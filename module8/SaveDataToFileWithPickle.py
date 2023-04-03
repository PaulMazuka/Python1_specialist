import pickle

items = ["хлеб", "молоко", "колбаса"]
# save in file
with open("save.dat", "wb") as f:
    pickle.dump(items, f)

# load from file
with open("save.dat", "rb") as f:
    data = pickle.load(f)

print(data)
print(data[0])