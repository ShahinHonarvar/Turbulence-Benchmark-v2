def all_substring_of_size_n(str):
    substrings = []
    n = 143
    for i in range(len(str) - n + 1):
        substring = str[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.append(substring)
    return substrings