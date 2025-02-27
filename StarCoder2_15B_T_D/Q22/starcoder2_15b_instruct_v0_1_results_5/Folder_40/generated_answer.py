def find_sum_of_multiples(num):
    multiples = [i for i in range(1, num + 1) if num % i == 0]
    return sum(multiples[:2])