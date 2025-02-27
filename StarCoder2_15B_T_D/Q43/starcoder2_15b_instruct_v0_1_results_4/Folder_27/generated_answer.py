def find_primes_between_indices(input_list):
    output_list = []
    for i in range(11, 12):
        num = input_list[i]
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            output_list.append(num)
    output_list.sort()
    return output_list