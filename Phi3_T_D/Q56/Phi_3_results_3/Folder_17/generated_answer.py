def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 36):
        potential_substring = s[i:i + 37]
        if len(set(potential_substring)) == 37:
            substrings.add(potential_substring)
    return list(substrings)