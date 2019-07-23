ip = input().split(",")
s = ""
for i in ip:
    name, rollno = i.split(":")
    l = len(name)
    rollno_int = list(map(int, list(rollno)))
    maxi = -1
    for j in rollno_int:
        if j <= l and j > maxi:
            maxi = j
    if maxi == -1:
        s += "X"
    elif maxi <= l:
        s += name[maxi-1]
print(s)
