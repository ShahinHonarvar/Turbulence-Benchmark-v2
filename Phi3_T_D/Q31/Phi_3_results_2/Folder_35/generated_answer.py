def if_perfect_num(numbers):
    index_993 = 993 if len(numbers) > 993 else -1
    if index_993 != -1:
        num = numbers[index_993]
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    return False