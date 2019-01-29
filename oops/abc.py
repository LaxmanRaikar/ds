import json
json_data=open("by.json").read()
data=json.loads(json_data)
print("\n")
for i in data["rice"]:
    total=int(i["weight"])*int(i["price"])
    print(i["name"],total,"per kg")
print("\n")
for j in data["pulses"]:
    total_pulses=int(j["weight"])*int(j["price"])
    print(j["name"],total_pulses,"per kg")
print("\n")

for k in data["wheats"]:
    total_wheat=int(k["weight"])*int(k["price"])
    print(k["name"],total_wheat,"per kg")

