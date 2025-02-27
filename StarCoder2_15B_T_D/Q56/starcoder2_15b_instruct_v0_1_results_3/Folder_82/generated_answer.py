def all_substring_of_size_n(string):
    n = 100
    distinct_substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            distinct_substrings.append(substring)
    return distinct_substrings