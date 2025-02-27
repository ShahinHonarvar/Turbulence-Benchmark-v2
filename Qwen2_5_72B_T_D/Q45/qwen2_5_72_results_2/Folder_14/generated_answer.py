from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:6].lower()
    letter_counts = {}
    for letter in substring:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    potential_palindromes = set()
    for length in range(3, 7):
        for perm in permutations(substring, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                potential_palindromes.add(perm_str)
    return potential_palindromes