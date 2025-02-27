from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    letter_counts = {char: substring.count(char) for char in set(substring)}
    palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes