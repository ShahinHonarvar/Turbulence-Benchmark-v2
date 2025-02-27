def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 98):
        substring = string[i:i + 99]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)