lst1 = [8,3,9,6,5,1,2,4,7]
k = 1
n = 9
lst7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def main():
    #order_2(subtract_2(lst1,k,n))
    #shift_1(lst1)
    dict_order(subtract_2([17, 9, 7, 19, 11, 15, 3, 14, 10, 18, 13, 2, 8, 16, 12, 6, 4, 5, 1, 20], 2000000000000000000, 20))

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
        print("current_carry: ", current_carry)
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
    print("final_list: ", final_list[::-1])
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
        print(first_append)
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
    print(final_list[::-1])
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
    print(mylist)
    return mylist

if __name__ == "__main__":
    main()
