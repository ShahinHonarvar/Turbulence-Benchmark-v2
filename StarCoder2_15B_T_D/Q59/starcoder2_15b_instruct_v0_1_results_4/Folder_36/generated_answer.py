def all_left_truncatable_prime(numbers):
    x = numbers[992]
    left_truncatable_prime = []
    for i in range(2, x):
        is_left_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            if not is_prime(int(str(i)[j + 1:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_prime.append(i)
    return sorted(left_truncatable_prime)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True