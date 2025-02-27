from itertools import permutations

def palindromes_between_indices(s: str):
    substring = s[2:7]
    unique_chars = set(substring.lower())
    palindromes = set()
    for i in range(5, len(substring) + 1):
        combos = permutations(unique_chars, i)
        for combo in combos:
            if combo == combo[::-1]:
                palindrome = ''.join(combo)
                palindromes.add(palindrome)
    return palindromes