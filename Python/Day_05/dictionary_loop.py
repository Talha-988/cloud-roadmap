employee = {
    "name": "Ali",
    "department": "IT",
    "salary": 80000,
    "city": "Karachi"
}

for keys in employee:
    print(keys)
for values in employee.values():
    print(values)
for keys, values in employee.items():
    print(f"{keys} : {values}")

