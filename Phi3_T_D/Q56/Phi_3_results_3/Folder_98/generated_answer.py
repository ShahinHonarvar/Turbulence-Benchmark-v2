from itertools import permutations

def all_substring_of_size_n(s):
    max_length = len(s)
    substrings = set()
    for i in range(max_length - 9):
        substr = s[i:i + 10]
        unique_chars = set(substr)
        if len(unique_chars) == 10:
            substrings.add(substr)
    resulted_substrings = []
    for perm in permutations(substrings, 10):
        unique_permutation = ''.join(set(''.join(perm)))
        if len(unique_permutation) == 10 and unique_permutation not in resulted_substrings:
            resulted_substrings.append(unique_permutation)
    return resulted_substrings