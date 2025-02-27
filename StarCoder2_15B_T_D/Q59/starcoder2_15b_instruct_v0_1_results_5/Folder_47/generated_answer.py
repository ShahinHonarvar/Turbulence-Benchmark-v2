def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    result = []
    digits = [1, 2, 3, 5, 7, 9]

    def generate_prime(current, digits_left):
        if digits_left == 0:
            n = int(''.join(map(str, current)))
            if is_prime(n) and n < x:
                result.append(n)
        else:
            for digit in digits:
                generate_prime(current + [digit], digits_left - 1)
    generate_prime([], len(str(x)))
    return sorted(result)