def if_perfect_num(numbers):
    index = 926
    num = numbers[index]
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num