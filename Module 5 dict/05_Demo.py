items = {"title": "Кепка",
         # {"colors"}: ["black", "red", "white"]
         "cost": 1300
         }
items["cost"] = 1500
items["brand"] = "Nike"
print(items["cost"])
print(items)

# del item["colors"]
print(items)

items2 = [
    {
        "title": "Кепка",
        "color": "black",
        "cost": 1300
    },
    {
        "title": "Pants",
        "color": "red",
        "cost": 2000

    },
    {
        "title": "shirts",
        "color": "white",
        "cost": 2500
    }
]
for num, item in enumerate(items2,1):
    print(f"{num}. {item['title']}")
