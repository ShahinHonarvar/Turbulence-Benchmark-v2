def if_perfect_num(numbers):
    return sum(numbers[702]) == sum([i for i in range(1, numbers[702]) if numbers[702] % i == 0])