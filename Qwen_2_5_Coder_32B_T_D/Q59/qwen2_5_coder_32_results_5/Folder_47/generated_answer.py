def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[49]
    result = []
    for num in range(2, x):
        snum = str(num)
        if '0' not in snum:
            truncatable = True
            for i in range(len(snum)):
                if not is_prime(int(snum[i:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return result