from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    letter_counts = {letter: substring.count(letter) for letter in set(substring)}
    possible_palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            possible_palindromes.add(candidate)
    return possible_palindromes