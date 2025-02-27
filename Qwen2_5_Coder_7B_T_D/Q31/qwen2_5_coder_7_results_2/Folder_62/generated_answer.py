def if_perfect_num(num_list):
    if len(num_list) > 926:
        num = num_list[926]
        sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum += i
                if i != num // i:
                    sum += num // i
        return sum == num and num != 1
    else:
        return False