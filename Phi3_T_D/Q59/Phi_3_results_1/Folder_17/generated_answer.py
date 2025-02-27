def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(rng):
    x = rng[35]
    truncatables = []
    for number in range(7, x, 2):
        str_num = str(number)
        left_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                left_truncatable = False
                break
        if left_truncatable:
            truncatables.append(number)
    return sorted(truncatables, reverse=True)