def all_left_truncatable_prime(args):
    x = args[24]
    result = []
    for i in range(2, x):
        is_left_truncatable = True
        num_str = str(i)
        for j in range(len(num_str)):
            truncated_num = int(num_str[j:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(i)
    return sorted(result)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True