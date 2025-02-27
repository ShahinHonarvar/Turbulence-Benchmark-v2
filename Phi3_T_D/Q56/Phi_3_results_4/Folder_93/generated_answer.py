def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 53):
        potential_substring = s[i:i + 54]
        if len(set(potential_substring)) == 54:
            substrings.add(potential_substring)
    return list(substrings)