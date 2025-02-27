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

def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[7]
    left_truncatables = []
    for num in range(23, x):
        if is_prime(num):
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                left_truncatables.append(num)
    return left_truncatables