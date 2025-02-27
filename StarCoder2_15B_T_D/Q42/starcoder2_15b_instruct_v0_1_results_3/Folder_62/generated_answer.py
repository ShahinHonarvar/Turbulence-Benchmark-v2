def prime_factors(my_list):
    num = my_list[926]
    prime_factors = []
    for i in range(2, num + 1):
        if num % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_factors.append(i)
    return prime_factors