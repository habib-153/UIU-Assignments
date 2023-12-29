f = open("c:/Python-Uni/Assignment_1_File+Dictionary/Task_1/statements.txt")
info = f.readlines()
# print(info)
name = ""
suspects = {}
lst1 = []
temp = []

for line in info:
    line = line.strip()
    if line != "-":
        temp.append(line)
    else:
        if temp:
            lst1.append(temp)
            temp = []
if temp:
    lst1.append(temp)
# print(lst1)

for i in lst1:
    name = i[0]
    # print(name)
    suspects[name] = {"alibi": i[1], "behavior": i[2]}
# print(suspects)

culprit = ""
for key,value in suspects.items():
    if "arguing with the museum curator" in value["behavior"]:
        culprit = key
        break
    
w = open("c:/Python-Uni/Assignment_1_File+Dictionary/Task_1/culprit.txt", "w")
w.write(f"{culprit} is the culprit because {suspects[culprit]['behavior']}")