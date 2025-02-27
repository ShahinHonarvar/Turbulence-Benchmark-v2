def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    result = []
    for num in range(0, num_tuple[71]):
        if is_prime(num):
            truncatable = True
            for i in range(len(str(num)) - 1, 0, -1):
                if not is_prime(int(str(num)[:i])):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    result.sort(reverse=True)
    return result