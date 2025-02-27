def if_perfect_num(numbers):
    if len(numbers) > 20:
        num = numbers[20]
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