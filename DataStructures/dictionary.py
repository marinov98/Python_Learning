students = {
            "Alice": {"id": "ID0001", "age": 26, "grade":"A"},
            "Bob": {"id": "ID0002", "age": 27, "grade":"B"},
            "Claire": {"id": "ID0003", "age": 17, "grade":"C"},
            "Dan": {"id": "ID0004", "age": 21, "grade":"D"},
            "Emma":{"id": "ID0005", "age": 22, "grade":"E"}
            }

print(students["Dan"]["age"])

print(students["Emma"]["id"], students["Emma"]["grade"])
students = {}
students = {"Alice": 25,"Bob": 27,"Claire": 17, "Dan": 21, "Emma": 22}
students["Fred"] = 25
students["Fred"] # 25
students.keys() # all first
a = list(students.keys())
list(students.values())[2:]
# do not use an index no order
students = {
    "Alice": ["ID0001", 26]
    "Bob": ["ID0003"], 25
    "Claire": 17,
    "Dan": 21,
    "Emma": 22
}
