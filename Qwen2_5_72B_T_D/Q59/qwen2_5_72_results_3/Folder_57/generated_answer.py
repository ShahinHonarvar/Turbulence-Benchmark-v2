def all_left_truncatable_prime(numbers):
    x = numbers[54]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            truncatable = True
            str_num = str(num)
            if '0' in str_num:
                truncatable = False
            else:
                for i in range(1, len(str_num)):
                    if not is_prime_number(int(str_num[i:])):
                        truncatable = False
                        break
            if truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True