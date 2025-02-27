from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9].lower()
    chars = ''.join(filter(lambda c: c.isalpha(), substring))
    found_palindromes = set()
    for length in range(4, 9):
        for perm in permutations(chars, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes