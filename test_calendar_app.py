import os
import calendar_app


def setup_function():
    if os.path.exists(calendar_app.DATA_FILE):
        os.remove(calendar_app.DATA_FILE)


def test_add_and_list(tmp_path):
    calendar_app.DATA_FILE = tmp_path / "data.json"
    calendar_app.add_event("2024-01-01", "10:00", "New Year Celebration")
    events = calendar_app.list_events("2024-01-01")
    assert events == {"2024-01-01": [{"time": "10:00", "description": "New Year Celebration"}]}


def test_remove(tmp_path):
    calendar_app.DATA_FILE = tmp_path / "data.json"
    calendar_app.add_event("2024-01-02", "09:00", "Meeting")
    calendar_app.add_event("2024-01-02", "15:00", "Another Meeting")
    calendar_app.remove_event("2024-01-02", 0)
    events = calendar_app.list_events("2024-01-02")
    assert events == {"2024-01-02": [{"time": "15:00", "description": "Another Meeting"}]}
