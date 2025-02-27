from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10]
    unique_chars = set(substring.lower())
    possible_palindromes = set()
    for r in range(7, 10):
        for combo in permutations(unique_chars, r):
            if combo == combo[::-1]:
                possible_palindromes.add(''.join(combo))
    return possible_palindromes