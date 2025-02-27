def prime_factors(numbers):
    number_at_index_410 = numbers[410]
    for i in range(2, number_at_index_410 + 1):
        if number_at_index_410 % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                return i