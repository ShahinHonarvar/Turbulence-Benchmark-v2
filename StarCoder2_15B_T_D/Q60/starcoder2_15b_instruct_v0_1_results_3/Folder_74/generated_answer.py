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

def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[36]
    result = []
    for num in range(1, x + 1):
        if is_prime(num):
            truncatable = True
            for i in range(len(str(num)) - 1):
                if not is_prime(int(str(num)[i:])) or not is_prime(int(str(num)[:len(str(num)) - i])):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return sorted(result)