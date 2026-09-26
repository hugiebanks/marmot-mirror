# Marmot Mirror 🦫

A small Discord interaction workbench for making and checking JSON fixtures. It lives in one HTML file, so there’s no bot, server, account, or install step. Open it when you need an interaction payload to test your code with.

## Open it

Download [`index.html`](index.html) and open it in a browser. It works offline; nothing is sent anywhere. Pick an example from the menu, edit the JSON, and save it with **Download**.

The examples cover:

- Slash commands
- Button clicks
- Modal submits
- Autocomplete

## What it does

The shape check catches common issues, like invalid JSON, a missing interaction type, or a missing `custom_id`. It’s a quick lint, not a full copy of Discord’s schema, so your app can still reject a payload that passes here.

Use **Format** to tidy the JSON or **Copy** to put it on your clipboard. **Scrub IDs** replaces values under fields named `id`, `application_id`, `guild_id`, `channel_id`, and `webhook_id` with a placeholder. It doesn’t remove usernames, message text, or every kind of personal information, so read through the fixture before sharing it.

## Optional command-line check

If you have Python 3 installed, you can check a fixture from a terminal too. No extra Python packages are needed:

```sh
python fixture_lint.py interaction.json
```

It prints any issues it finds and exits with a non-zero status if the fixture needs a look. This is handy for a small script or a local build step.

## Privacy

The HTML workbench runs entirely in your browser. It doesn’t make network requests, read files from your computer, or save your edits after you close the page. Use **Download** if you want to keep a fixture.

The sample payloads use fake IDs and names. If you paste a real interaction into the editor, it stays in that browser tab; the scrub button only replaces the ID fields listed above. Check the whole JSON before you post it publicly.

## Files

- `index.html` — the offline browser tool; this is all most people need.
- `fixture_lint.py` — optional Python command-line checker.

Marmot Mirror doesn’t connect to Discord or run your bot. It helps you make fixture JSON to use in your own tests and development setup.
