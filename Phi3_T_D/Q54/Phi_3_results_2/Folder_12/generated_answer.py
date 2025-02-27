def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(*, tuple_of_ints):
    x = tuple_of_ints[70]
    all_primes = []
    for num in range(x - 1, 1, -1):
        temp = num
        is_rtprime = True
        while is_prime(temp):
            is_rtprime = temp < x
            temp //= 10
        if is_rtprime:
            all_primes.append(num)
    return sorted(all_primes, reverse=True)