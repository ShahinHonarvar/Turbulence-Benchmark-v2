def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[685]) if numbers[685] % i == 0]) == numbers[685]