def return_n_greatest_chars(string):
    distinct_chars = list(string)
    sorted_chars = sorted(distinct_chars, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:59]