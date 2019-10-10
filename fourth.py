lst = [8, 3, 9, 6, 4, 7, 5, 2, 1]

def main():
    test(lst)

def test(lst):
    line_one = []
    reverse_line_two = lst
    shifted_num = []
    reverse_line_two = reverse_line_two[::-1]
    limit = len(reverse_line_two)
    for i in range(limit):
        line_one.append(i + 1)
    line_one.pop(0)
    left = reverse_line_two[:i]
    right = reverse_line_two[i:]
    reverse_line_two1 = reverse_line_two[1:]
    for i in range(len(reverse_line_two1)):
        count = 0
        if i == 0:
            for j in left:
                if j < reverse_line_two1[i]:
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

#def order(lst):





if __name__ == '__main__':
    main()
