import json

def load_schema(event_type):
    event_schema_template = f"schemas/{event_type}.json"
    
    try:
        with open(event_schema_template, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"ERROR: Facing issues in reading schema for {event_type}")
        return None