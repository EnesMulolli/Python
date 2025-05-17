data = {
    "name":"Enes",
    "age":17,
    "address": {
        "city":"Prishtina",
        "street":"123 street"
    },
    "contact":[
        {
            "type":"email"
        },
        {
            "type":"phone"
        }
    ]
}

print(data["name"])
print(data["address"]["city"])
print(data["contact"][1])