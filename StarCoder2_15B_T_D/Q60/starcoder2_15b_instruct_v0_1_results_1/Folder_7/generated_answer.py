def all_left_right_truncatable_prime(args):
    left_right_truncatable_primes = []
    for num in args:
        if num > 0:
            num_str = str(num)
            if '0' not in num_str:
                is_left_right_truncatable = True
                for i in range(len(num_str)):
                    if not is_prime(int(num_str[i:])):
                        is_left_right_truncatable = False
                        break
                    if not is_prime(int(num_str[:len(num_str) - i])):
                        is_left_right_truncatable = False
                        break
                if is_left_right_truncatable:
                    left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True