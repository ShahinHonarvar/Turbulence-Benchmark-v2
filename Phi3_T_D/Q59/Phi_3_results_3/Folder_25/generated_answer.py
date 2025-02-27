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

def all_left_truncatable_prime(numbers, x_index=92):
    x = numbers[x_index]
    truncatables = []
    for num in range(2, x):
        num_str = str(num)
        if all((is_prime(int(num_str[i:])) for i in range(len(num_str)))):
            truncatables.append(num)
    return sorted(truncatables)