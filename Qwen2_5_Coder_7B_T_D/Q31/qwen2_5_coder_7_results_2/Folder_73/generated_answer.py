def if_perfect_num(numbers):
    if len(numbers) > 41:
        num = numbers[41]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    return False