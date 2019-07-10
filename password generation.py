op_number = ""
input_number = input()
for i in range(len(input_number)):
    if int(input_number[i])%2 == 1:
        op_number+=str(int(input_number[i])**2)
if(len(op_number)<=4):
    print(op_number)
else:
    print(op_number[0:4])
