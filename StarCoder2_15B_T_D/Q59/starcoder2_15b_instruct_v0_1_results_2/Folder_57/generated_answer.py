def all_left_truncatable_prime(args):
    x = args[0]
    result = []
    for num in range(2, x):
        is_truncatable = True
        temp = num
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp = temp % 10 ** len(str(temp))
        if is_truncatable:
            result.append(num)
    return sorted(result, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True