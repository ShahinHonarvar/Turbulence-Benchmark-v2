def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[835]
    result = []
    for n in range(10, x + 1):
        if is_prime(n):
            s = str(n)
            if set(s) == {'1', '3', '7', '9'}:
                for i in range(len(s) - 1):
                    if not is_prime(int(s[i + 1:])) or not is_prime(int(s[:i + 1])):
                        break
                else:
                    result.append(n)
    return sorted(result)