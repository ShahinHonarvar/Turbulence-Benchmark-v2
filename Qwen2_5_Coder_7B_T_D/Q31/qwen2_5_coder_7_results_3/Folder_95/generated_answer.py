def if_perfect_num(numbers):
    if len(numbers) > 87:
        num = numbers[87]
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    else:
        return False