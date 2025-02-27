def find_primes_between_indices(int_list):

    def is_prime(num):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        return False
    return sorted([num for num in int_list[36:96] if is_prime(num)], reverse=True)