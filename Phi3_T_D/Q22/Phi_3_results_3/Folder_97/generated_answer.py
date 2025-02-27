def find_sum_of_multiples(integer):
    start = integer
    end = integer * 210
    multiples_sum = sum(range(start, end + 1, integer))
    return multiples_sum