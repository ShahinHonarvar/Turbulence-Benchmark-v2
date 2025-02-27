def if_perfect_num(numbers):
    index = 90
    if index < len(numbers):
        num = numbers[index]
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    return False