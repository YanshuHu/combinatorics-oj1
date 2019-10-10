top = [2,3,4,5,6,7,8,9]
a = [8,3,9,7,4,1,5,6]
b = [8,3,9,6,4,7,5,2,1]
# lst = [1,0,0,4,5]
lst = [7, 2, 6, 4, 3, 0, 0, 1]
new_list = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
k = [9,9,0,0,0]
index = 1
value = 2
lst1 = [8, 3, 9, 6, 5, 1]
comparator = 1
lst4 = [8,3,9,6,5,1,2]


def main():
    test3(lst)

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




def test3(lst):
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
            print("lst: ", mylist[:i], "current_carry: ", current_carry, "smaller: ", smaller)
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
        if i not in temp:
            no.append(i)
    for i in range(len(mylist)):
        if mylist[i] == -1:
            mylist[i] = no[0]
    print(mylist)



def test2(lst):
    limit = len(lst) + 1
    temp = []
    print(lst)
    for i in range(limit):
        temp.append(-1)
    for i in range(len(lst)):
        bigger = False
        current_carry = lst[i] + 1
        print(current_carry, lst[i])
        if i == 0:
            temp[0] = current_carry
        temp1 = temp
        print(temp1)
        for j in range(len(temp1[:i])):
            if j == 6:
                print(current_carry, temp1[:i][j], temp1, temp1[:i])
            if temp1[:i][j] < (current_carry):
                current_carry += 1
                temp[i] = current_carry
                #print("line 30 current_carry: ", current_carry)
            elif current_carry not in temp[:i]:
                temp[i] = current_carry
                #print("line 33 current_carry: ", current_carry)
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

def test1(a,b):
    left = []
    no = []
    print(len(b))
    print(len(a))
    for i in a:
        left.append(i)
    for i in b:
        if i not in a:
            no.append(i)
    print(left)
    print(no)



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
    for i in range(len(temp)):
        if temp[i] == -1:
            temp[i] = 1
    print(temp)

def test(new_list, index, value):
    num = 0
    a = new_list
    for i in range(len(new_list)):
        print(i)
        if new_list[i] == -1:
            num+=1
            if num == index+1:
                new_list[i] = value
    print(num, new_list)


def find_it_3(new_list,index,value):
    num = 0
    for i in range(len(new_list)):
        if new_list[i] == -1:
            num+=1
            if num == index+1:
                new_list[i] = value
    return new_list



def order(lst):
    new_lst = lst[::-1]
    new_top = top[::-1]
    temp = []
    for i in range(len(new_lst)+1):
        temp.append(-1)
    print("new_lst:", new_lst, "new_top: ", new_top, "temp: ", temp)
    for i in range(len(new_lst)):
        temp = find_it(temp, new_lst[i], new_top[i])

            # print("temp values: ", temp[val], temp)
    for i in range(len(temp)):
        if temp[i] == -1:
            temp[i] = 1
    print(temp[::-1])
    # print(new_top)
    # print(new_lst)
    # print(temp[::-1])




if __name__ == "__main__":
    main()
