n = int(input())
l = list(map(int, input().split()))
index_diff_list = []
d = {}
l1 = []
prev_crate_index = 0
prev_peak_index = 0
for i in range(n - 1, 0, -1):
    val = l[i] - l[i - 1]
    if val < 0 :
        d[i] = "crate"
    else:
        d[i] = "peak"
if l[0] - l[1] < 0:
    d[0] = "crate"
else:
    d[0] = "peak"
for i in range(1, n-1):
    val = l[i] - l[i + 1]
    if val < 0 and d[i] == "crate":
        l1.append(i - prev_crate_index)
        prev_crate_index = i
    elif val > 0 and d[i] == "peak":
        l1.append(i - prev_peak_index)
        prev_peak_index = i
if d[n - 1] == "crate":
    l1.append(n - 1 - prev_crate_index)
else:
    l1.append(n - 1 - prev_peak_index)
print(max(l1))        
