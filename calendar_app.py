import argparse
import json
from pathlib import Path

DATA_FILE = Path('calendar_data.json')


def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_event(date, time, description):
    data = load_data()
    events = data.setdefault(date, [])
    events.append({"time": time, "description": description})
    save_data(data)


def list_events(date=None):
    data = load_data()
    if date:
        events = data.get(date, [])
        return {date: events}
    return data


def remove_event(date, index):
    data = load_data()
    events = data.get(date)
    if not events:
        raise ValueError("No events on that date")
    if index < 0 or index >= len(events):
        raise IndexError("Event index out of range")
    events.pop(index)
    if not events:
        data.pop(date)
    else:
        data[date] = events
    save_data(data)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Simple schedule management")
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('--date', required=True, help='YYYY-MM-DD')
    parser_add.add_argument('--time', required=True, help='HH:MM')
    parser_add.add_argument('--description', required=True)

    parser_list = subparsers.add_parser('list')
    parser_list.add_argument('--date', help='YYYY-MM-DD')

    parser_remove = subparsers.add_parser('remove')
    parser_remove.add_argument('--date', required=True, help='YYYY-MM-DD')
    parser_remove.add_argument('--index', type=int, required=True)

    args = parser.parse_args(argv)

    if args.command == 'add':
        add_event(args.date, args.time, args.description)
    elif args.command == 'list':
        events = list_events(args.date)
        print(json.dumps(events, ensure_ascii=False, indent=2))
    elif args.command == 'remove':
        remove_event(args.date, args.index)


if __name__ == '__main__':
    main()
