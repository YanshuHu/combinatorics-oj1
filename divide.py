top = [2,3,4,5,6]
# lst = [1,0,0,4,5]
lst = [1,2,3,4,5]
k = [9,9,0,0,0]
lst1 = [8,3,9,6,4,7,5,2,1]
lst2 = [10,11,12,8,3,9,6,4,7,5,2,1]
lst3 = [8,9,3,6,7,4,5,2,1]
lst4 = [8,3,9,6,4,7,5,2,1]
k = [9,0,0,0,0,0,0,0]
k = k[::-1]


def main():
    subtract_1(lst1, k)

def helper1(lst, start):
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

def subtract_1(lst, k):
    print("top: ", top)
    print("lst: ", lst)
    print("k: ", k)
    subtract_list = []
    list_len = len(lst)
    next_borrow = 1
    for i in range(list_len):
        #print("the list of i is: ", i)
        #print("36 ",lst[i] - k[i], lst, k[i])
        if (lst[i] - k[i]) >= 0:
            #print("37 ",lst[i] - k[i], lst, k[i])
            subtract_list.append(lst[i] - k[i])
        while (lst[i] - k[i]) < 0:
            if lst[i+next_borrow] > 0:
                lst[i+next_borrow] -= 1
                lst[i] = lst[i] + top[i]
                if (lst[i] - k[i]) >= 0:
                    subtract_list.append(lst[i] - k[i])
                    #print("44 ",lst[i] - k[i], lst, k[i])
                    #print("43", lst[i] - k[i], lst[i], k[i])
                #print("44",lst[i] - k[i], lst[i], k[i])
            #problem!!!!!
            elif lst[i+next_borrow] == 0:
                a = helper1(lst, i)
                index_of_carry = a[0][0]
                index_of_zeros = a[1][0]
                #print(lst[index_of_carry])
                #print(lst[index_of_zeros])
                temp = lst[:index_of_carry]
                print(temp)
                #print("value of i at 52: ",i)
                #print("57", lst[i] - k[i], lst[i], k[i])
                lst[index_of_carry] -= 1
                for j in range(len(temp)):
                    #print("value of i at 54: ", i)
                    #print("61", lst[j] + top[j], lst, lst[3], j)
                    lst[j] += top[j]
                if (lst[i] - k[i]) > 0:
                    subtract_list.append(lst[i] - k[i])
                #print("value of i at 60: ",i)
                #print("61", lst[i] - k[i], lst[i], k[i])
            #problem!!!!!
    print("subtract_list:", subtract_list)

if __name__ == "__main__":
    main()
