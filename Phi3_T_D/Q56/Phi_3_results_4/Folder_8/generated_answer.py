def all_substring_of_size_n(input_str):
    n = 30
    unique_substrings = set()
    for i in range(len(input_str) - n + 1):
        substring = input_str[i:i + n]
        if len(set(substring)) == n:
            unique_substrings.add(substring)
    return list(unique_substrings)