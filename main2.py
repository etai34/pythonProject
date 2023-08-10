names = ["ofek", "idan", "eden", "aviran"]
a = "guy"

for i in range(len(names)):
    if a == names[i]:
        b = 1

    else:
        b = 0

if b == 1:
    print("guy is on the list")
else:
    print("guy is not on the list")

if "guy" in names:
    print("guy is on the list") 
else:
    print("guy is not on the list")