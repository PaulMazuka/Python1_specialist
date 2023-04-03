import json

items = ["хлеб", "молоко", "колбаса"]

# save data to file

with open("save.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False)


#load from file
with open("save.json", "r", encoding="utf-8") as f:
    data=json.load(f)

print(data)
print(data[0])