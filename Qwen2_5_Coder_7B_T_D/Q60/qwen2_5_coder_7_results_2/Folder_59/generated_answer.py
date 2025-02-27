def all_left_right_truncatable_prime(numbers):
    x = numbers[84]
    primes = [2, 3, 5, 7]
    all_truncatable_primes = []
    for num in range(11, x + 1):
        if all((int(digit) != 0 and is_prime(num) for digit in str(num))):
            is_truncatable = True
            str_num = str(num)
            while len(str_num) > 1:
                if not is_prime(int(str_num[:len(str_num) - 1])) or not is_prime(int(str_num[1:])):
                    is_truncatable = False
                    break
                str_num = str_num[1:-1]
            if is_truncatable:
                all_truncatable_primes.append(num)
    return sorted(all_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True