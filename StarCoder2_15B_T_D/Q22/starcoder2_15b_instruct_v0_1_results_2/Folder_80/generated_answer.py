def find_sum_of_multiples(n: int) -> int:
    first_term = n
    last_term = 276 * n
    num_of_terms = 276
    sum_of_multiples = (first_term + last_term) * num_of_terms // 2
    return sum_of_multiples