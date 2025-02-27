def all_substring_of_size_n(input_string):
    unique_substrings = set()
    n = 149
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(set(substring)) == n:
            unique_substrings.add(substring)
    return list(unique_substrings)