lst1 = [8,3,9,6,4,7,5,2,1]
k = 12419
n = 9
lst7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def main():
    #order_2(subtract_2(lst1,k,n))
    order_2(subtract_2([1, 17, 11, 20, 7, 15, 13, 10, 6, 16, 12, 19, 8, 18, 5, 3, 4, 14, 9, 2], 2000000000000000000, 20))

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
        print("first_carry: ", first_carry)
        first_append = step_one%line_one[0]
        print("first_append: ", first_append)
        final_list.append(first_append)
    if step_one < line_one[0]:
        first_carry = 0
        first_append = step_one%line_one[0]
        final_list.append(first_append)
    index = 1
    current_carry = first_carry
    print(reverse_line_two)
    while index < (n -1):
        print("current_carry: ", current_carry)
        if (reverse_line_two[index]) + current_carry >= line_one[index]:
            res = reverse_line_two[index] + current_carry
            current_carry = res//line_one[index]
            print("appending: ",res%line_one[index])
            final_list.append(res%line_one[index])
            index += 1
        if (reverse_line_two[index] + current_carry) < line_one[index]:
            res1 = reverse_line_two[index] + current_carry
            current_carry = 0
            print("appending: ",res1%line_one[index])
            final_list.append(res1)
            index += 1
    print("final_list: ", final_list)
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
    print(step_one)
    if step_one < 0:
        first_carry = -((step_one) // line_one[0])
        print(first_carry)
        first_append = step_one%line_one[0]
        print(first_append)
        final_list.append(first_append)
    if step_one >= 0:
        first_carry = 0
        first_append = step_one%line_one[0]
        final_list.append(first_append)
    index = 1
    current_carry = first_carry
    print("final_list: ", final_list)
    while index < (n-1):
        #print("current_carry: ", current_carry)
        print("index: ", reverse_line_two[index])
        print(reverse_line_two[index] - current_carry)
        if reverse_line_two[index] - current_carry < 0:
            res = reverse_line_two[index] - current_carry
            print("res: ",res)
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
    print(final_list)
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
    print(temp[::-1])
    return temp[::-1]


if __name__ == "__main__":
    main()
