def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if not is_prime(num):
            continue
        num_str = str(num)
        i = 1
        while i < len(num_str):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                break
            i += 1
        else:
            result.append(num)
    result.sort(reverse=True)
    return result