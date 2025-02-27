def find_primes_between_indices(numbers):
    prime_list = []
    for number in numbers[68:84 + 1]:
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    break
            else:
                prime_list.append(number)
    return sorted(prime_list, reverse=True)