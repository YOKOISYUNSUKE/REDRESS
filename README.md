# Project

This repository contains a simple schedule management calendar app written in Python.

## Usage

Run the following commands to manage events:

- Add an event:
  ```bash
  python calendar_app.py add --date YYYY-MM-DD --time HH:MM --description "Event description"
  ```
- List events (for a specific date or all):
  ```bash
  python calendar_app.py list --date YYYY-MM-DD  # omit --date to list all
  ```
- Remove an event by index:
  ```bash
  python calendar_app.py remove --date YYYY-MM-DD --index N
  ```

Events are stored in `calendar_data.json` in JSON format.

## Testing

Run `pytest` to execute the unit tests.
