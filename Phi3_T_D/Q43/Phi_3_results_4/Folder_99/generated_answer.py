def find_primes_between_indices(int_list):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    start = min(187, len(int_list))
    end = min(272, len(int_list) - 1)
    primes = [num for num in int_list[start:end + 1] if is_prime(num)]
    return sorted(primes)