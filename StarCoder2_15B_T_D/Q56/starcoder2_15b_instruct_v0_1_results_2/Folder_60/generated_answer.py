def all_substring_of_size_n(input_string):
    n = 36
    substrings = []
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.append(substring)
    return substrings