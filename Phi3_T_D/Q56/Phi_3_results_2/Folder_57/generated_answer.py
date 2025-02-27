from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 60, len(s) + 1):
            substr = s[i:j]
            if len(substr) == 60 and len(set(substr)) == 60:
                result.add(substr)
    return list(result)