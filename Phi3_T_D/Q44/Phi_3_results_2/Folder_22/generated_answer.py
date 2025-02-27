def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(numbers):
    composites = set()
    for num in numbers[50:201]:
        if not is_prime(num):
            composites.add(num)
    return composites