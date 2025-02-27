def all_left_truncatable_prime(input_tuple):
    x = input_tuple[18]
    result = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i)) - 1):
            truncated_num = int(str(i)[j + 1:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable and is_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True