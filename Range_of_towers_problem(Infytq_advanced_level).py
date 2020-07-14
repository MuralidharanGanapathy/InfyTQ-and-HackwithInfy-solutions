def traceback(l,t):
    l1 = []
    for i in l:
        if i <= t:
            l1.append(i)
    return max(l1)


range_of_tower = int(input())
l = list(map(int, input().split()))
d = {}
for i in range(len(l) - 2, 0, -1):
    if l[i] - l[i - 1] > 0:
        d[i] = "peak"
peak_indices = []
for i in range(1, len(l) - 1):
    if i in d.keys() and l[i] - l[i + 1] > 0 and d[i] == "peak":
        peak_indices.append(i)
tower = -1
count = 0
while(tower < len(l)):
    tower += range_of_tower
    if tower >= len(l):
        break
    tower = traceback(peak_indices, tower)
    count += 1
print(count)
    
