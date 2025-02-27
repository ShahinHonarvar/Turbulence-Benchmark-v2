def all_substring_of_size_n(string):
    unique_substrings = set()
    for i in range(len(string) - 67 + 1):
        substring = string[i:i + 67]
        if len(set(substring)) == 67:
            unique_substrings.add(substring)
    return list(unique_substrings)