from faker import Faker
from datetime import datetime
from schema_loader import load_schema 
from configs.config import (
    EVENT_TYPES,
    PRODUCT_CATEGORIES,
    PAYMENT_METHODS,
    DEVICE_TYPES,
    EVENT_SOURCES
)
import random
import uuid
import json

fake = Faker()

def generate_event(schema):
    event = schema

    if "event_id" in event: event["event_id"] = str(uuid.uuid4())
    if "event_source" in event: event["event_source"] = random.choice(EVENT_SOURCES)
    if "event_timestamp" in event: event["evenevent_timestampt_source"] = datetime.now().isoformat()
    if "user_id" in event: event["user_id"] = fake.uuid4()
    if "session_id" in event: event["session_id"] = fake.uuid4()
    if "country_code" in event: event["country_code"] = fake.country_code()
    if "device_type" in event: event["device_type"] = random.choice(DEVICE_TYPES)

    if "product_id" in event: event["product_id"] = fake.uuid1()
    if "product_price" in event: event["product_price"] = fake.pricetag()
    if "product_name" in event: event["product_name"] = fake.word().title()
    if "category" in event: event["category"] = random.choice(PRODUCT_CATEGORIES)

    if "order_id" in event: event["order_id"] = fake.uuid4()
    if "order_amount" in event: event["order_amount"] = round(random.uniform(20, 5000), 2)
    if "payment_mode" in event: event["payment_mode"] = random.choice(PAYMENT_METHODS)

    return event

event_type = random.choice(EVENT_TYPES)
schema = load_schema(event_type)

if schema:
    print(f"Returned Schema Template for event type : {event_type}")
    print(schema)
    
    event_json = generate_event(event_type, schema)
    print(f"Generated event : {print(json.dumps(event_json, indent=2))}")
else:
    print(f"No Schema found for {event_type}")