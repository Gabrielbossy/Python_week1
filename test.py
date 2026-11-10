import json

try:
    with open("test.json") as f:
        loaded = json.load(f)
except FileNotFoundError:
    loaded = {}

print(loaded)