def all_substring_of_size_n(input_string):
    n = 44
    substrings = set()
    for i in range(len(input_string) - n + 1):
        potential_sub = input_string[i:i + n]
        if len(set(potential_sub)) == n:
            substrings.add(potential_sub)
    return list(substrings)