from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10]
    char_set = ''.join(filter(str.isalpha, substring.lower()))
    found_palindromes = set()
    for length in range(3, len(char_set) + 1):
        for perm in permutations(char_set, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes