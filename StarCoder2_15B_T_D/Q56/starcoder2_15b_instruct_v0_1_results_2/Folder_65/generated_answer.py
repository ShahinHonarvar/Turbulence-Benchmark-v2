def all_substring_of_size_n(my_string):
    n = 81
    substrings = []
    for i in range(len(my_string) - n + 1):
        substring = my_string[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.append(substring)
    return substrings