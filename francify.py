import os
import yaml


z = os.listdir("localization")
# print(z)
for fp in z:
    l = open("localisation\\" + fp, "r", encoding="UTF-8")
    lines = l.readlines()
    sp = None
    nl = []
    temp = ""
    nl.append(lines[0])
    for x in lines[1:]:
        if x.find("#") == -1:
            sp = x.split(" \"")
            tmp = sp[0] + " \"France\"\n"
            nl.append(tmp)
    l.close()
    l = open("localization\\" + fp, "w", encoding="UTF-8")
    for x in nl:
        l.write(x)
    l.close()


print(nl)
