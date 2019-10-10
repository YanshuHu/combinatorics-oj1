# lst1 = [8,3,9,6,4,7,5,2,1]
# lst2 = [10,11,12,8,3,9,6,4,7,5,2,1]
# lst3 = [8,9,3,6,7,4,5,2,1]
# lst4 = [8,3,9,6,4,7,5,2,1]
# lst = [7, 2, 6, 4, 2, 3, 2, 1]
# lst5 = [14, 4, 8, 17, 16, 2, 12, 6, 18, 3, 10, 13, 9, 5, 1, 11, 19, 15, 7, 20]
# lst6 = [1, 17, 11, 20, 7, 15, 13, 10, 6, 16, 12, 19, 8, 18, 5, 3, 4, 14, 9, 2]
# lst7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# k3 = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# #k = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,2,0]
# k1 = [0,0,0,0,4,0,2,0]
# k2 = [0,0,0,0,0,0,0,1]

#[9, 1, 1]
#[8, 3, 9, 6, 4, 7, 5, 2, 1]

# 9 1 1
# 8 3 9 6 4 7 5 2 1

def main():
    variable1 = input()
    variable2 = input()
    a = variable1.split()
    b = variable2.split()
    first_line = []
    second_line = []
    # k = variable1.split()
    # print(k)
    #get inputs
    for i in a:
        first_line.append(int(i))
        #print(int(i))
    for i in b:
        second_line.append(int(i))
    #what kind of order
    add = True
    type = first_line[1]
    if first_line[2] >= 0:
        add = True
    if first_line[2] < 0:
        add = False
    lst = second_line
    k = abs(int(first_line[2]))
    k = [int(i) for i in str(k)]
    # missing_k = 0
    missing_k = 20 - len(k)
    k = k[::-1]
    for i in range(missing_k):
        k.append(0)
    k = k[::-1]
    if type == 1:
        if add == True:
            output = dict_order(add_1(second_line, k))
        else:
            output = dict_order(subtract_1(second_line, k))
    if type == 2:
        if add == True:
            output = order_2(add_2(second_line, k))
        else:
            output = order_2(subtract_2(second_line, k))
    if type == 3:
        if add == True:
            output = order_3(add_3(second_line,k))
        else:
            output = order_3(subtract_3(second_line, k))
    final = ' '.join(str(i) for i in output)
    print(final)
    #print(lst)
    #print(k)
    #print(add)
    #order_3(add_3(lst1 , k))
    #order_2(add_2(lst7, k3))
    #shift_3(lst1)

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
    #print("shifted_num: ", shifted_num)
    return shifted_num

def add_1(lst1, k):
    shifted_num = shift_1(lst1)
    limit = len(shifted_num) + 1
    limit_list = []
    added_list = []
    k = k[::-1]
    for i in range(limit):
        limit_list.append(i + 1)
    limit_list.pop(0)
    #the list i want to work with
    true_list = shifted_num[::-1]
    #print("here",true_list)
    list_len = len(true_list)
    for i in range(list_len):
        if (true_list[i]+k[i]) > limit_list[i]:
            true_list[i+1] += 1
            a = (true_list[i] + k[i]) - (limit_list[i])
            added_list.append(a)
        elif (true_list[i]+k[i]) == limit_list[i]:
            if len(true_list) != 1:
                true_list[i+1] += 1
            else:
                true_list.append(1)
            added_list.append(0)
        else:
            added_list.append(true_list[i] + k[i])
            #print("here", true_list )
    #print("limit_list: ", limit_list)
    #print("added_list: ", added_list[::-1])
    return added_list[::-1]


def helper1(lst, start):
    new_lst = lst[start:]
    index_of_zeros = []
    index_of_carry = []
    for i in range(len(new_lst)):
        if new_lst[i] == 0:
            index_of_zeros.append(i+ start)
        elif new_lst[i] > 0:
            index_of_carry.append(i)
    #print(index_of_carry, start)
    index_of_carry = index_of_carry[1] + start
    a = []
    a.append([index_of_carry])
    a.append(index_of_zeros)
    return a

def subtract_1(lst, k):
    shifted_num = shift_1(lst)
    limit_list = []
    k = k[::-1]
    limit = len(shifted_num) + 1
    for i in range(limit):
        limit_list.append(i + 1)
    limit_list.pop(0)
    top = limit_list
    lst = shifted_num[::-1]
    subtract_list = []
    list_len = len(lst)
    next_borrow = 1
    #print(top)
    for i in range(list_len):
        if (lst[i] - k[i]) >= 0:
            subtract_list.append(lst[i] - k[i])
        while (lst[i] - k[i]) < 0:
            if lst[i+next_borrow] > 0:
                lst[i+next_borrow] -= 1
                lst[i] = lst[i] + top[i]
                if (lst[i] - k[i]) >= 0:
                    subtract_list.append(lst[i] - k[i])
            elif lst[i+next_borrow] == 0:
                a = helper1(lst, i)
                index_of_carry = a[0][0]
                index_of_zeros = a[1][0]
                temp = lst[:index_of_carry]
                lst[index_of_carry] -= 1
                for j in range(len(temp)):
                    lst[j] += top[j]
                if (lst[i] - k[i]) > 0:
                    subtract_list.append(lst[i] - k[i])
    #print("subtract_list:", subtract_list[::-1])
    return subtract_list[::-1]

def dict_order(lst):
    limit = len(lst) + 1
    temp = []
    for i in range(limit):
        temp.append(-1)
    for i in range(len(lst)):
        bigger = False
        current_carry = lst[i] + 1
        if i == 0:
            temp[0] = current_carry
        for j in temp[:i]:
            if j <= (current_carry):
                current_carry += 1
                temp[i] = current_carry
                j = -10
            elif current_carry not in temp[:i]:
                temp[i] = current_carry
        while (current_carry) in temp[:i]:
            current_carry += 1
            temp[i] = current_carry
    left = []
    no = []
    for i in range(len(temp)):
        left.append(i+1)
    for i in left:
        if i not in temp:
            no.append(i)
    for i in range(len(temp)):
        if temp[i] == -1:
            temp[i] = no[0]
    print(temp)
    return temp
###############

###############加
def shift_2(lst):
    new_lst = lst
    shifted_num = []
    #print(new_lst)
    while new_lst:
        count = 0
        biggest = max(new_lst)
        biggest_index = new_lst.index(biggest)

        # for i in range(len(new_lst[biggest_index:])):
        #     #print(new_lst[biggest_index:])
        #     if new_lst[i] < biggest:
        #         #print(new_lst[i],biggest)
        #         count += 1
        for i in new_lst[biggest_index+1:]:
            #print(new_lst[biggest_index:])
            if i < biggest:
                #print(new_lst[i],biggest)
                count += 1
        shifted_num.append(count)
        del new_lst[biggest_index]
    shifted_num.pop()
    #print("shifted_num: ", shifted_num)
    return shifted_num[::-1]

##### add them using the algorithm

def add_2(lst, k):
    shifted_num = shift_2(lst)
    limit = len(shifted_num) + 1
    limit_list = []
    added_list = []
    k = k[::-1]
    for i in range(limit):
        limit_list.append(i + 1)
    limit_list.pop(0)
    #the list i want to work with
    true_list = shifted_num
    limit_list = limit_list
    #print("limit_list: ", limit_list)
    #print("true_list: ", true_list)
    #print("k: ", k)
    list_len = len(true_list)
    for i in range(list_len):
        if (true_list[i]+k[i]) > limit_list[i]:
            true_list[i+1] += 1
            a = (true_list[i] + k[i]) - (limit_list[i])
            added_list.append(a)
        elif (true_list[i]+k[i]) == limit_list[i]:
            if len(true_list) != 1:
                true_list[i+1] += 1
            else:
                true_list.append(1)
            added_list.append(0)
        else:
            added_list.append(true_list[i] + k[i])
    #print(added_list[::-1])
    return added_list[::-1]

def helper2(lst, start):
    new_lst = lst[start:]
    index_of_zeros = []
    index_of_carry = []
    for i in range(len(new_lst)):
        if new_lst[i] == 0:
            index_of_zeros.append(i+ start)
        elif new_lst[i] > 0:
            index_of_carry.append(i)
    index_of_carry = index_of_carry[1] + start
    a = []
    a.append([index_of_carry])
    a.append(index_of_zeros)
    #print("a:", a)
    return a

def subtract_2(lst, k):
    shifted_num = shift_2(lst)
    limit_list = []
    shifted_num = shifted_num[::-1]
    k = k[::-1]
    limit = len(shifted_num) + 1
    for i in range(limit):
        limit_list.append(i + 1)
    limit_list.pop(0)
    top = limit_list
    lst = shifted_num[::-1]
    subtract_list = []
    list_len = len(lst)
    next_borrow = 1
    #print("top: ",top)
    #print(k)
    #print(lst)
    for i in range(list_len):
        if (lst[i] - k[i]) >= 0:
            subtract_list.append(lst[i] - k[i])
        while (lst[i] - k[i]) < 0:
            if lst[i+next_borrow] > 0:
                lst[i+next_borrow] -= 1
                lst[i] = lst[i] + top[i]
                if (lst[i] - k[i]) >= 0:
                    subtract_list.append(lst[i] - k[i])
            elif lst[i+next_borrow] == 0:
                a = helper1(lst, i)
                index_of_carry = a[0][0]
                index_of_zeros = a[1][0]
                temp = lst[:index_of_carry]
                lst[index_of_carry] -= 1
                for j in range(len(temp)):
                    lst[j] += top[j]
                if (lst[i] - k[i]) > 0:
                    subtract_list.append(lst[i] - k[i])
    print("subtract_list:", subtract_list)
    return subtract_list[::-1]

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
    a = shift_2(lst)
    a = a[::-1]
    #print(a[::-1])
    return a[::-1]

    # print (lst)
#add 中介数
def add_3(lst, k):
    shifted_num = shift_3(lst)
    limit = len(shifted_num) + 1
    limit_list = []
    added_list = []
    k = k[::-1]
    for i in range(limit):
        limit_list.append(i + 1)
    limit_list.pop(0)
    true_list = shifted_num[::-1]
    limit_list = limit_list[::-1]
    list_len = len(true_list)
    for i in range(list_len):
        if (true_list[i]+k[i]) > limit_list[i]:
            true_list[i+1] += 1
            a = (true_list[i] + k[i]) - (limit_list[i])
            added_list.append(a)
        elif (true_list[i]+k[i]) == limit_list[i]:
            if len(true_list) != 1:
                true_list[i+1] += 1
            else:
                true_list.append(1)
            added_list.append(0)
        else:
            added_list.append(true_list[i] + k[i])
    #print(added_list[::-1])
    return added_list[::-1]

#subtraction helper
def helper3(lst, start):
    new_lst = lst[start:]
    index_of_zeros = []
    index_of_carry = []
    for i in range(len(new_lst)):
        if new_lst[i] == 0:
            index_of_zeros.append(i+ start)
        elif new_lst[i] > 0:
            index_of_carry.append(i)
    index_of_carry = index_of_carry[1] + start
    a = []
    a.append([index_of_carry])
    a.append(index_of_zeros)
    return a

#subtract 中介数
def subtract_3(lst, k):
    shifted_num = shift_3(lst)
    limit_list = []
    k = k[::-1]
    limit = len(shifted_num) + 1
    for i in range(limit):
        limit_list.append(i + 1)
    limit_list.pop(0)
    top = limit_list[::-1]
    #reverse list to work with
    lst = shifted_num[::-1]
    subtract_list = []
    list_len = len(lst)
    next_borrow = 1
    for i in range(list_len):
        if (lst[i] - k[i]) >= 0:
            subtract_list.append(lst[i] - k[i])
        while (lst[i] - k[i]) < 0:
            if lst[i+next_borrow] > 0:
                lst[i+next_borrow] -= 1
                lst[i] = lst[i] + top[i]
                if (lst[i] - k[i]) >= 0:
                    subtract_list.append(lst[i] - k[i])
            elif lst[i+next_borrow] == 0:
                a = helper1(lst, i)
                index_of_carry = a[0][0]
                index_of_zeros = a[1][0]
                temp = lst[:index_of_carry]
                lst[index_of_carry] -= 1
                for j in range(len(temp)):
                    lst[j] += top[j]
                if (lst[i] - k[i]) > 0:
                    subtract_list.append(lst[i] - k[i])
    #print("subtract_list:", subtract_list)
    return subtract_list[::-1]

#find value helper
def find_it_3(new_list,index,value):
    num = 0
    for i in range(len(new_list)):
        if new_list[i] == -1:
            num+=1
            if num == index+1:
                new_list[i] = value
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
    temp = []
    for i in range(len(new_lst)+1):
        temp.append(-1)
    # print("new_lst:", new_lst, "new_top: ", new_top, "temp: ", temp)
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
def shift_4(lst):
    new_lst = lst
    shifted_num = []
    while new_lst:
        count = 0
        biggest = max(new_lst)
        biggest_index = new_lst.index(biggest)
        for i in range(len(new_lst[biggest_index:])):
            if new_lst[i] < biggest:
                count += 1
        shifted_num.append(count)
        del new_lst[biggest_index]
    shifted_num.pop()
    a = shifted_num[::-1]
    return a

if __name__ == "__main__":
    main()
