def composite_nums_between_indices(numbers):
    prime_nums = set()
    composite_nums = set()
    for num in numbers:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if not is_prime:
            composite_nums.add(num)
    for i, num in enumerate(numbers):
        if i >= 30 and i <= 87 and (num not in prime_nums):
            composite_nums.add(num)
    return composite_nums