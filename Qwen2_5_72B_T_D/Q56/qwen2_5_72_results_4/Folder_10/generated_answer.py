def all_substring_of_size_n(s):
    n = 55
    substrings = [s[i:i + n] for i in range(len(s) - n + 1)]
    unique_substrings = []
    for substring in substrings:
        if len(set(substring)) == n:
            unique_substrings.append(substring)
    return unique_substrings