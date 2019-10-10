lst1 = [8,3,9,6,4,7,5,2,1]
lst2 = [10,11,12,8,3,9,6,4,7,5,2,1]
lst3 = [8,9,3,6,7,4,5,2,1]
lst4 = [8,3,9,6,4,7,5,2,1]
lst = [7, 2, 6, 4, 2, 3, 2, 1]
lst5 = [14, 4, 8, 17, 16, 2, 12, 6, 18, 3, 10, 13, 9, 5, 1, 11, 19, 15, 7, 20]
lst6 = [1, 17, 11, 20, 7, 15, 13, 10, 6, 16, 12, 19, 8, 18, 5, 3, 4, 14, 9, 2]
lst7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
k3 = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#k = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,2,0]
k1 = [0,0,0,0,4,0,2,0]
k2 = [0,0,0,0,0,0,0,5]

def main():
    add_1(lst1, k2)

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
    print("shifted_num: ", shifted_num)
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
    print("here",true_list)
    list_len = len(true_list)
    print(k)
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
    print(added_list[::-1])
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
    return temp

if __name__ == "__main__":
    main()
