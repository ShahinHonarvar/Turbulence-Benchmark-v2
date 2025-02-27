def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 11):
        substring = string[i:i + 12]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)