def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    left_truncatable = [2, 3, 5, 7]
    right_truncatable = [2, 3, 5, 7]
    for i in range(1, len(str(x))):
        for j in range(1, 10):
            if is_prime(int(str(j) + str(i))):
                left_truncatable.append(int(str(j) + str(i)))
            if is_prime(int(str(i) + str(j))):
                right_truncatable.append(int(str(i) + str(j)))
    truncatable = list(set(left_truncatable) & set(right_truncatable))
    return sorted([t for t in truncatable if t <= x])