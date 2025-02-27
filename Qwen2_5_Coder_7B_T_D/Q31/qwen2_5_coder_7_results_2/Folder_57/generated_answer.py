def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[92]) if numbers[92] % i == 0]) == numbers[92]