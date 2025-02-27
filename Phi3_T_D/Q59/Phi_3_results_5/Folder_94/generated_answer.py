def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[43]
    results = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            while len(s) > 1:
                s = s[1:]
                if not is_prime(int(s)):
                    break
            else:
                results.append(i)
    return results