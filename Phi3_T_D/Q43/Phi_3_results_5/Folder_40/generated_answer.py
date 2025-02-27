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

def find_primes_between_indices(lst):
    sorted_lst = [num for num in lst]
    sorted_lst.sort()
    max_index = len(sorted_lst)
    return [num for num in sorted_lst if is_prime(num) and 1 <= lst.index(num) <= max_index]