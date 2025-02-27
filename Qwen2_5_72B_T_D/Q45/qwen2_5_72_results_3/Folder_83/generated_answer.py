from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:10]
    letter_counts = [substring.lower().count(char) for char in set(substring.lower()) if char.isalpha()]
    possible_palindromes = set()
    for perm in permutations(substring.lower()):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 7:
            possible_palindromes.add(candidate)
    return possible_palindromes