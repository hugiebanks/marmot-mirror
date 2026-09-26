import json, sys
from pathlib import Path

def check(thing):
  probs = []
  if type(thing) != dict:
    return ["this needs to be an object, not whatever that is"]

  if thing.get('type') not in [1, 2, 3, 4, 5]:
    probs.append('type is missing or weird')
  if not thing.get("token"):
    probs.append("no token in here")
  if thing.get('version') != 1:
    probs.append("version is usually 1")
  if not thing.get('application_id'):
    probs.append("application_id is missing")

  kind = thing.get('type')
  data = thing.get("data")
  if kind == 2 or kind == 4:
    if not isinstance(data, dict):
      probs.append("probably want a data object for this one")
    elif not data.get("name"):
      probs.append("data.name is missing")

  if kind == 3 or kind == 5:
    if not isinstance(data, dict) or not data.get('custom_id'):
      probs.append("forgot the data.custom_id")

  if (thing.get('guild_id') or thing.get('channel_id')) and not thing.get('member') and not thing.get('user'):
    probs.append("server interaction but no member/user??")

  return probs

def main():
  if len(sys.argv) != 2:
    print("usage: python fixture_lint.py interaction.json")
    return 1

  file = Path(sys.argv[1])
  try:
    text = file.read_text(encoding='utf-8')
    obj = json.loads(text)
  except FileNotFoundError:
    print("can't find", file)
    return 1
  except json.JSONDecodeError as e:
    print("json is busted on line", e.lineno, "column", e.colno)
    return 1
  except OSError as e:
    print("reading it didn't work:", e)
    return 1

  problems = check(obj)
  if problems:
    print(str(file) + " has stuff to fix:")
    for p in problems:
      print(" - " + p)
    return 1

  print(str(file) + " looks ok i guess")
  return 0

if __name__ == "__main__":
  sys.exit(main())
