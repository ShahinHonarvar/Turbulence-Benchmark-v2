from sympy import primerange, isprime

def composite_nums_between_indices(num_list):
    composite_set = set()
    for i in range(90, 201):
        if not isprime(num_list[i]) and num_list[i] > 1:
            composite_set.add(num_list[i])
    return composite_set