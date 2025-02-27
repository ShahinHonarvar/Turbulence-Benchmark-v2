def find_primes_between_indices(lst):
    prime_numbers = []
    for number in lst[43:77]:
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    break
            else:
                prime_numbers.append(number)
    return sorted(prime_numbers, reverse=True)