def all_substring_of_size_n(input_string):
    n = 94
    substrings = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)