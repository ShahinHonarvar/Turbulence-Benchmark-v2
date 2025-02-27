def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generates_rt_primes(n):
    if is_prime(n):
        yield str(n)
    if n < 10:
        return
    for i in range(1, 10):
        if n % 10 == i:
            next_str = str(n)[:-1] + str(i)
            if is_prime(int(next_str)):
                yield next_str

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    result = []
    for number in numbers:
        if number < x:
            rt_primes = list(generates_rt_primes(number))
            result.extend(rt_primes)
    return sorted(list(set(result)))