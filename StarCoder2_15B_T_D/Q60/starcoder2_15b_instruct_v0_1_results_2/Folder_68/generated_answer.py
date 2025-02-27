def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    output = []
    for i in range(10, x + 1):
        if is_prime(i):
            j = i
            while j >= 10:
                j //= 10
                if not is_prime(j):
                    break
            else:
                output.append(i)
    return sorted(output, reverse=True)