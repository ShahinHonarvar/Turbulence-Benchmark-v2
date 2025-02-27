def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(args):
    x = args[1]
    truncatables = []
    for num in range(x, 1, -1):
        num_str = str(num)
        if '0' in num_str or len(num_str) < 2:
            continue
        is_truncatable = True
        for i in range(1, len(num_str) // 2 + 1):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatables.append(num)
    return truncatables