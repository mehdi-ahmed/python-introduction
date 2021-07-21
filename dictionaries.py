# key/value pairs

# Each key should be unique..
customer = {
    "name": "Mehdi",
    "age": "39",
    "country": "BE",
    "is_verified": True
}

print(customer["age"])  # 39
# print(customer["unbound"])  # KeyError: 'unbound'

print(customer.get("name"))  # Mehdi
print(customer.get("unbound"))  # None

# We can add a new key or modify an existing one
customer["name"] = "Marcus"
customer["height"] = "1m80"

print(customer)   # {'name': 'Marcus', 'age': '39', 'country': 'BE', 'is_verified': True, 'height': '1m80'}
