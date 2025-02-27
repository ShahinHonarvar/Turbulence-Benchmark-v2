from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:9].lower()
    letter_counts = {char: substring.count(char) for char in set(substring)}
    possible_palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 3:
            possible_palindromes.add(candidate)
    return possible_palindromes