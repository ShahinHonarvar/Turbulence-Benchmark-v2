from itertools import combinations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if len(set(substring)) == 92:
            result.add(substring)
    return list(result)