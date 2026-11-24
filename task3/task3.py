import sys
import json

if len(sys.argv) != 4:
    print("Использованы 3 файла")
    sys.exit(1)

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

with open(values_file, "r", encoding="utf-8") as file:
    values_data = json.load(file)

with open(tests_file, "r", encoding="utf-8") as file:
    tests_data = json.load(file)

results = {}

for item in values_data["values"]:
    results[item["id"]] = item["value"]

def fill_values(item):
    if isinstance(item, dict):
        if "id" in item and item["id"] in results and "value" in item:
            item["value"] = results[item["id"]]

        for value in item.values():
            fill_values(value)

    elif isinstance(item, list):
        for element in item:
            fill_values(element)

fill_values(tests_data)

with open(report_file, "w", encoding="utf-8") as file:
    json.dump(tests_data, file, ensure_ascii=False, indent=4)