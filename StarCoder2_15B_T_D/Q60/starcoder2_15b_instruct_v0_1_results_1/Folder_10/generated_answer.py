def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[38]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_left_right_truncatable_prime(num):
    if num < 10:
        return False
    if num in (11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
        return True
    if num < 100:
        return False
    return is_left_right_truncatable_prime(int(str(num)[1:])) and is_left_right_truncatable_prime(int(str(num)[:-1]))