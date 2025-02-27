def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        all_prime = True
        temp = str_num
        while len(temp) > 1:
            if not is_prime(int(temp)) or not is_prime(int(temp[1:])):
                all_prime = False
                break
            temp = temp[1:-1]
        if all_prime and is_prime(int(temp)):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)