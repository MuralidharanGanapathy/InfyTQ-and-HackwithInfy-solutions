def validate(l1, l2):
    for i in range(2):
        if l1[i] > l2[i]:
            return l2
    return l1

stack1 = []
input_list = sorted(map(int, input().split(",")))
for i in range(len(input_list)-2):
    top = -1
    stack = []
    for k in range(i+1,len(input_list)-1):
        top = -1
        stack.append(input_list[i])
        stack.append(input_list[k])
        top+=2
        for j in range(k+1,len(input_list)):
            if stack[top] + stack[top-1] == input_list[j]:
                stack.append(input_list[j])
                top+=1
        if len(stack1) < len(stack):
            stack1 = stack
        elif len(stack1) == len(stack):
            stack1 = validate(stack1, stack)
        stack = []
    stack = []
print(' '.join(list(map(str,stack1))))
