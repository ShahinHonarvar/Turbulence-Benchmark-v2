def if_perfect_num(num_list):
    if len(num_list) > 632:
        num = num_list[632]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
        else:
            return False
    else:
        return False