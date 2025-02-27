def find_sum_of_multiples(num):
    multiples = [i for i in range(1, num + 1) if num % i == 0]
    sum_of_multiples = sum(multiples[:3])
    return sum_of_multiples