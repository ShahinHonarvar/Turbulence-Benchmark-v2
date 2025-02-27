def all_substring_of_size_n(s):
    n = 120
    n_set = set()
    substrings = set()
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n:
            n_set.add(s[i:i + n])
    for substring in n_set:
        substrings.add(''.join(sorted(substring)))
    return list(substrings)