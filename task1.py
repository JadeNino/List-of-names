import sys
names = [
    ['Alice', 'Bob', 'Charlie'],
    ['David', 'Eve', 'Frank'],
    ['Grace', 'Heldi', 'Ivan'],
    ['Judy', 'Ken', 'Laura']
]
pangalan = input("Enter a name : ")

for name in names:
    for get_name in name:
        if pangalan == get_name:
            names.pop([0][0])
            print("Alice has been remove")
            print(names)
            sys.exit()
        else:
            user = input("Enter a name : ")
            names.append(user)
            print("Nice one")
            print(names)
            sys.exit
