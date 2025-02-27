def all_left_right_truncatable_prime(tup):
    x = tup[0]
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        is_left_right_truncatable = True
        current_num = num
        while len(str(current_num)) > 1:
            if not is_prime(current_num):
                is_left_right_truncatable = False
                break
            current_num = int(str(current_num)[1:])
            if not is_prime(current_num):
                is_left_right_truncatable = False
                break
            current_num = int(str(current_num)[:-1])
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True