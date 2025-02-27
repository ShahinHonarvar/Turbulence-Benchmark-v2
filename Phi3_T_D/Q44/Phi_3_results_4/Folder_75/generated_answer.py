def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(data):
    composites = {num for num in data[75:86] if not is_prime(num) and num > 1}
    return composites