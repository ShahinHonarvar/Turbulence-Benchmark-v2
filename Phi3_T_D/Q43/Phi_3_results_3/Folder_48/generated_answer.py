def find_primes_between_indices(lst):
    prime_numbers = []
    for number in lst[260:460]:
        if number > 1:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(number)
    return sorted(prime_numbers)