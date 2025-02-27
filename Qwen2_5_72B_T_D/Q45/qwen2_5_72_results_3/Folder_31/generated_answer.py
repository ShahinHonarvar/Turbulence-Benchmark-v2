from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9].lower()
    letter_counts = {char: substring.count(char) for char in set(substring)}
    potential_palindromes = set()
    for perm in permutations(substring):
        test_str = ''.join(perm)
        if test_str == test_str[::-1] and len(test_str) >= 6:
            potential_palindromes.add(test_str)
    return potential_palindromes