lst = [1, 0, 1, 2, 1, 3, 7, 2]
lst1 = [8, 3, 9, 6, 4, 7, 5, 2, 1]
lst7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

n = 20
k = 2000000000000000000

def main():
    shift_4(subtract_4([1,2,3],1,3))


def shift_4(lst):
    line_one = []
    #print(lst)
    reverse_line_two = lst
    #print(reverse_line_two)
    shifted_num = []
    reverse_line_two = reverse_line_two[::-1]
    #print(reverse_line_two)
    limit = len(reverse_line_two)
    #print(limit)
    for i in range(limit):
        line_one.append(i + 1)
    line_one.pop(0)
    left = reverse_line_two[:i]
    right = reverse_line_two[i:]
    reverse_line_two1 = lst[1:]
    #print(len(reverse_line_two1))
    #print("line_one: ", line_one, "reverse_line_two: ", reverse_line_two, "reverse_line_two1: ", reverse_line_two1)
    for i in range(len(reverse_line_two1)):
        count = 0
        if i == 0:
            for j in left:
                if line_one[i] > j:
                    count+=1
            shifted_num.append(count)
        if i > 0:
            if line_one[i] % 2 == 1:
                if shifted_num[i-1]%2 ==0:
                    for j in reverse_line_two[:reverse_line_two.index(line_one[i])]:
                        if line_one[i] > j:
                            count+=1
                    shifted_num.append(count)
                elif shifted_num[i-1]%2 ==1:
                    for j in reverse_line_two[reverse_line_two.index(line_one[i]):]:
                        if line_one[i] > j:
                            count+=1
                    shifted_num.append(count)
            elif line_one[i] % 2 == 0:
                if (shifted_num[i-1]+shifted_num[i-2])%2 ==0:
                    for j in reverse_line_two[:reverse_line_two.index(line_one[i])]:
                        if line_one[i] > j:
                            count+=1
                    shifted_num.append(count)
                if (shifted_num[i-1]+shifted_num[i-2])%2 ==1:
                    for j in reverse_line_two[reverse_line_two.index(line_one[i]):]:
                        if line_one[i] > j:
                            count+=1
                    shifted_num.append(count)
    print(shifted_num)
    return shifted_num

def add_4(lst, k, n):
    line_two = shift_4(lst)
    #bound
    line_one = []
    #Easier to manipulate in list notation
    reverse_line_two = line_two[::-1]
    #subtracted list i want
    final_list = []
    #length of the bounds
    limit = len(reverse_line_two) + 1
    for i in range(limit):
        line_one.append(i + 1)
    line_one.pop(0)
    line_one = line_one[::-1]
    #print("line_one: ", line_one)
    #print("reverse_line_two: ", reverse_line_two)
    step_one = reverse_line_two[0] + k
    if step_one >= line_one[0]:
        first_carry = step_one//line_one[0]
        #print("first_carry: ", first_carry)
        first_append = step_one%line_one[0]
        #print("first_append: ", first_append)
        final_list.append(first_append)
    if step_one < line_one[0]:
        first_carry = 0
        first_append = step_one%line_one[0]
        final_list.append(first_append)
    index = 1
    current_carry = first_carry
    #print(reverse_line_two)
    #print(n)
    while index < (n -1):
        #print("current_carry: ", current_carry)
        #print("r: ",reverse_line_two,"index: ", index, "value: ",reverse_line_two[index])
        if (reverse_line_two[index]) + current_carry >= line_one[index]:
            res = reverse_line_two[index] + current_carry
            current_carry = res//line_one[index]
            #print("appending: ",res%line_one[index])
            final_list.append(res%line_one[index])
            index += 1
        if (reverse_line_two[index] + current_carry) < line_one[index]:
            res1 = reverse_line_two[index] + current_carry
            current_carry = 0
            #print("appending: ",res1%line_one[index])
            final_list.append(res1)
            index += 1
    #print("final_list: ", final_list)
    return final_list[::-1]



def subtract_4(lst, k, n):
    line_two = shift_4(lst)
    #bound
    line_one = []
    #Easier to manipulate in list notation
    reverse_line_two = line_two[::-1]
    #subtracted list i want
    final_list = []
    #length of the bounds
    limit = len(reverse_line_two) + 1
    for i in range(limit):
        line_one.append(i + 1)
    line_one.pop(0)
    line_one = line_one[::-1]
    step_one = reverse_line_two[0] - k
    #print(step_one)
    if step_one < 0:
        first_carry = -((step_one) // line_one[0])
        #print(first_carry)
        first_append = step_one%line_one[0]
        #print(first_append)
        final_list.append(first_append)
    if step_one >= 0:
        first_carry = 0
        first_append = step_one%line_one[0]
        final_list.append(first_append)
    index = 1
    current_carry = first_carry
    #print("final_list: ", final_list)
    print(reverse_line_two[index], current_carry)
    while index < (n-1):
        #print("current_carry: ", current_carry)
        #print("index: ", reverse_line_two[index])
        #print(reverse_line_two[index] - current_carry)
        if reverse_line_two[index] - current_carry < 0:
            res = reverse_line_two[index] - current_carry
            #print("res: ",res)
            final_list.append(res%line_one[index])
            current_carry = -(res//line_one[index])
            index += 1
        if reverse_line_two[index] - current_carry >= 0:
            res1 = reverse_line_two[index] - current_carry
            current_carry = 0
            final_list.append(res1)
            index += 1

    # print("line_one: ", line_one, "line_two: ", reverse_line_two)
    # print("append value: ",(reverse_line_two[0]-k)%line_one[0])
    # final_list.append((reverse_line_two[0]-k)%line_one[0])
    # print("carry value: ", first_carry, final_list)
    # print("carried: ",  reverse_line_two[1] - first_carry )
    # carried = reverse_line_two[1] - first_carry
    # second_append = (carried)%line_one[1]
    # final_list.append(second_append)
    #print(final_list)
    return final_list[::-1]

def find_it_4(new_list,index,value):
    num = 0
    for i in range(len(new_list)):
        if new_list[i] == -1:
            num+=1
            if num == index+1:
                new_list[i] = value
    return new_list

def find_it_neg_4(new_list,index,value):
    num = 0
    lst = new_list[::-1]
    for i in range(len(new_list)):
        if lst[i] == -1:
            num+=1
            if num == index+1:
                lst[i] = value
    a = lst[::-1]
    return a

def order_4(lst):
    lst1 = lst[::-1]
    limit = len(lst1)+1
    top = []
    mylist = []
    for i in range(limit):
        top.append(i + 1)
    top.pop(0)
    for i in range(limit):
        mylist.append(-1)
    b = top[::-1]
    #print(b,lst1,mylist)
    for i in range(len(lst1)):
        #print(mylist)
        if b[i] != 2:
            if b[i]%2 == 1:
                if lst1[i+1]%2 == 1:
                    mylist = find_it_4(mylist, lst1[i], b[i])
                    #mylist[lst1[i]] = b[i]
                elif lst1[i+1]%2 ==0:
                    mylist = find_it_neg_4(mylist, lst1[i], b[i])
                    print("find neg: ", mylist, lst1[i], b[i])
            elif b[i]%2 == 0:
                if (lst1[i+1]+lst1[i+2])%2 == 1:
                    mylist = find_it_4(mylist, lst1[i], b[i])
                    #mylist[lst1[i]] = b[i]
                elif (lst1[i+1]+lst1[i+2])%2 == 0:
                    mylist = find_it_neg_4(mylist, lst1[i], b[i])
                    print("find neg: ", mylist, lst1[i], b[i])

        #print(mylist, lst1[i], b[i])
        elif b[i] == 2:
            mylist = find_it_neg_4(mylist, lst1[i], b[i])
    for i in range(len(mylist)):
        #print(mylist, lst1[i], b[i])
        if mylist[i] == -1:
            mylist[i] = 1
    print(mylist)
    return mylist





if __name__ == '__main__':
    main()
