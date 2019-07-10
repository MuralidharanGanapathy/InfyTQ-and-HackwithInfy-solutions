inp = input()
inp_list = list(inp)
sp_index_list = []
sp_list = []
temp_list = []
count = 0
st = ""
for i in range(len(inp_list)):
    if inp_list[i].isupper() == False and inp_list[i].islower() == False:
        sp_index_list.append(i)
        sp_list.append(inp_list[i])
        count += 1
        #sp_list[i] = 0
    else:
        temp_list.append(inp_list[i])
temp_list = temp_list[::-1]
j = 0
for i in range(len(inp_list)):
    if len(sp_index_list)>0 and i == sp_index_list[0]:
        st+=sp_list[0]
        del sp_list[0]
        del sp_index_list[0]
    else:
        st+=temp_list[j]
        j+=1
print(st)

