prefix = "my name is"
names = ["ofek", "idan", "eden", "aviran", "avidan", "daniel"]
for name in names:
    name = name + "z"
    print(f"{prefix} {name}")


for i in range(len(names)):
    names[i] = names[i] + "x"
    print(f"{prefix} {names[i]}")

result = []
for name in names:
    if name.find("dan") > -1:
        result.append(name)

result = [name + "z" for name in names if name.find("dan") > -1]
for name in result:
    print(name)
print(result)

age = int(input("enter your age"))
while age < 50:
    print("you are still ok")
    age = int(input("enter your age"))
