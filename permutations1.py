def main():
    variable1 = input()
    variable2 = input()
    a = variable1.split()
    b = variable2.split()
    first_line = []
    second_line = []
    for i in a:
        first_line.append(int(i))
    for i in b:
        second_line.append(int(i))
    add = True
    type = first_line[1]
    n = first_line[0]
    if first_line[2] >= 0:
        add = True
    if first_line[2] < 0:
        add = False
    lst = second_line
    k = abs(int(first_line[2]))
    if type == 1:
        if add == True:
            output = dict_order(add_1(second_line, k, n))
        else:
            output = dict_order(subtract_1(second_line, k ,n))
    if type == 2:
        if add == True:
            output = order_2(add_2(second_line, k, n))
        else:
            output = order_2(subtract_2(second_line, k,n))
    if type == 3:
        if add == True:
            output = order_3(add_3(second_line,k, n))
        else:
            output = order_3(subtract_3(second_line, k,n))
    if type == 4:
        if add == True:
            output = order_4(add_4(second_line,k, n))
        else:
            output = order_4(subtract_4(second_line, k,n))
    final = ' '.join(str(i) for i in output)
    print(final)

############### 字典
def shift_1(lst):
    new_lst = lst
    shifted_num = []
    while new_lst:
        count = 0
        compare = new_lst[0]
        for i in range(len(new_lst)):
            if new_lst[i] < new_lst[0]:
                count += 1
        shifted_num.append(count)

        del new_lst[0]
    shifted_num.pop()
    return shifted_num

def add_1(lst, k, n):
    line_two = shift_1(lst)
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
    #print(reverse_line_two[0])
    #print(k)
    step_one = reverse_line_two[0] + k
    first_carry = step_one//line_one[0]
    if step_one >= line_one[0]:
        #first_carry = step_one//line_one[0]
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
    while index < (n -1):
        #print("current_carry: ", current_carry)
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
    #print("final_list: ", final_list[::-1])
    return final_list[::-1]



def subtract_1(lst, k, n):
    line_two = shift_1(lst)
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
    step_one = reverse_line_two[0] - k
    #print(step_one)
    if step_one < 0:
        first_carry = -((step_one) // line_one[0])
        first_append = step_one%line_one[0]
        #print(first_append)
        final_list.append(first_append)
    if step_one >= 0:
        first_carry = 0
        first_append = step_one%line_one[0]
        final_list.append(first_append)
    index = 1
    current_carry = first_carry
    #print("current_carry: ", current_carry)
    while index < (n-1):
        #print("current_carry: ", current_carry)
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
    #print(final_list[::-1])
    return final_list[::-1]

def num_smaller(lst, b):
    '''
    lst is the list from mylist[:i]
    b is the comparator which is current_carry
    '''
    current_carry = b
    while True:
        count = 0
        for i in range(len(lst)):
            if lst[i] < current_carry:
                #print("lst: ", lst, "current_carry: ", current_carry)
                count += 1
                lst[i] = 100
                current_carry += 1
        if count == 0:
            break
    #print(current_carry)
    return current_carry

def dict_order(lst):
    limit = len(lst) + 1
    mylist = []
    for i in range(limit):
        mylist.append(-1)
    for i in range(len(lst)):
        has_bigger = True
        current_carry = lst[i] + 1
        if i == 0:
            mylist[0] = (current_carry)
        temp = mylist[:i]
        if i > 0:
            smaller = num_smaller(mylist[:i],current_carry)
            #print("lst: ", mylist[:i], "current_carry: ", current_carry, "smaller: ", smaller)
            if smaller not in mylist[:i]:
                mylist[i] = smaller
            while (smaller) in mylist[:i]:
                smaller += 1
                mylist[i] = smaller
    left = []
    no = []
    for i in range(len(mylist)):
        left.append(i+1)
    for i in left:
        if i not in mylist:
            no.append(i)
    for i in range(len(mylist)):
        if mylist[i] == -1:
            mylist[i] = no[0]
    #print(mylist)
    return mylist
###############

###############加
def shift_2(lst):
    new_lst = lst
    line_two = []
    while new_lst:
        count = 0
        biggest = max(new_lst)
        biggest_index = new_lst.index(biggest)
        for i in new_lst[biggest_index+1:]:
            if i < biggest:
                count += 1
        line_two.append(count)
        del new_lst[biggest_index]
    line_two.pop()
    #print("line_two: ", line_two)
    return line_two

def add_2(lst, k, n):
    line_two = shift_2(lst)
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
    while index < (n -1):
        #print("current_carry: ", current_carry)
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



def subtract_2(lst, k, n):
    line_two = shift_2(lst)
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

def find_it_2(new_list,index,value):
    num = 0
    for i in range(len(new_list)):
        if new_list[i] == -1:
            num+=1
            if num == index+1:
                new_list[i] = value
    #print("new list: ", new_list )
    return new_list

#return from 中介数
def order_2(lst):
    top = []
    limit = len(lst) + 1
    for i in range(limit):
        top.append(i + 1)
    top.pop(0)
    new_top = top[::-1]
    new_lst = lst
    temp = []
    for i in range(len(new_lst)+1):
        temp.append(-1)
    #print("new_lst:", new_lst, "new_top: ", new_top, "temp: ", temp)
    for i in range(len(new_lst)):
        #print(new_lst:", new_lst, "new_top: ", new_top, "temp: ", temp)
        temp = find_it_2(temp, new_lst[i], new_top[i])
    for i in range(len(temp)):
        if temp[i] == -1:
            temp[i] = 1
    #print(temp[::-1])
    return temp[::-1]
    ###############增

###############减
#get 中介数
def shift_3(lst):
    new_lst = lst
    line_two = []
    while new_lst:
        count = 0
        biggest = max(new_lst)
        biggest_index = new_lst.index(biggest)
        for i in new_lst[biggest_index+1:]:
            if i < biggest:
                count += 1
        line_two.append(count)
        del new_lst[biggest_index]
    line_two.pop()
    #print("line_two: ", line_two)
    #print(line_two[::-1])
    return line_two[::-1]

def add_3(lst, k, n):
    line_two = shift_3(lst)
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
    while index < (n -1):
        #print("current_carry: ", current_carry)
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



def subtract_3(lst, k, n):
    line_two = shift_3(lst)
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

def find_it_3(new_list,index,value):
    num = 0
    for i in range(len(new_list)):
        if new_list[i] == -1:
            num+=1
            if num == index+1:
                new_list[i] = value
    print("new list: ", new_list)
    return new_list

#return from 中介数
def order_3(lst):
    top = []
    limit = len(lst) + 1
    for i in range(limit):
        top.append(i + 1)
    top.pop(0)
    new_top = top[::-1]
    new_lst = lst[::-1]
    #print("top: ",top, "new_lst: ", new_lst)
    temp = []
    for i in range(len(new_lst)+1):
        temp.append(-1)
    #print("new_lst:", new_lst, "new_top: ", new_top, "temp: ", temp)
    for i in range(len(new_lst)):
        #print(new_lst:", new_lst, "new_top: ", new_top, "temp: ", temp)
        temp = find_it_3(temp, new_lst[i], new_top[i])
    for i in range(len(temp)):
        if temp[i] == -1:
            temp[i] = 1
    #print(temp[::-1])
    return temp[::-1]
###############加

###############邻排列
# def shift_4(lst):
#     new_lst = lst
#     shifted_num = []
#     while new_lst:
#         count = 0
#         biggest = max(new_lst)
#         biggest_index = new_lst.index(biggest)
#         for i in range(len(new_lst[biggest_index:])):
#             if new_lst[i] < biggest:
#                 count += 1
#         shifted_num.append(count)
#         del new_lst[biggest_index]
#     shifted_num.pop()
#     a = shifted_num[::-1]
#     return a
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
            #print(shifted_num)
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
    #print("shifted_num: ",shifted_num)
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
    while index < (n -1):
        #print("current_carry: ", current_carry)
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
                    #print("find neg: ", mylist, lst1[i], b[i])
            elif b[i]%2 == 0:
                if (lst1[i+1]+lst1[i+2])%2 == 1:
                    mylist = find_it_4(mylist, lst1[i], b[i])
                    #mylist[lst1[i]] = b[i]
                elif (lst1[i+1]+lst1[i+2])%2 == 0:
                    mylist = find_it_neg_4(mylist, lst1[i], b[i])
                    #print("find neg: ", mylist, lst1[i], b[i])
        elif b[i] == 2:
            #print("b: ", b, "i: ", i, "lst1: ", lst1)
            #print(mylist)
            #print("mylist: ", mylist, "lst1[i]： ", lst1[i], "b[i]： ", b[i])
            mylist = find_it_neg_4(mylist, lst1[i], b[i])
    left = []
    no = []
    for i in range(len(mylist)):
        left.append(i+1)
    for i in left:
        if i not in mylist:
            no.append(i)
    for i in range(len(mylist)):
        if mylist[i] == -1:
            mylist[i] = no[0]
    #print(mylist)
    return mylist

if __name__ == "__main__":
    main()
