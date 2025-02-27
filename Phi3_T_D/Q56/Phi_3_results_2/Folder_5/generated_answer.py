def all_substring_of_size_n(input_str):
    substrings = set()
    n = 64
    for i in range(len(input_str) - n + 1):
        substring = input_str[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)