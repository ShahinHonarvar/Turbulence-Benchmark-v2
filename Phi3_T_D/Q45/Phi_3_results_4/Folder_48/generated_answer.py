import itertools

def palindromes_between_indices(s):
    palindromes = set()
    substring = s[6:9].lower()
    letter_counts = {}
    for letter in substring:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    if len(substring) >= 8 or (('a' in letter_counts or 'b' in letter_counts) and len(substring) >= 6):
        combos = itertools.combinations_with_replacement(letter_counts.keys(), 4)
        for combo in combos:
            if len(set(combo)) == 1 or 'a' in combo or 'b' in combo:
                palindrome_center = sorted(''.join(combo))
                for perm in itertools.product(palindrome_center, repeat=2):
                    if len(set(perm)) != 1:
                        palindrome = ''.join(sorted(perm + combo)) + ''.join(sorted(perm, reverse=True))
                        palindromes.add(palindrome)
        for perm in itertools.product(palindrome_center, repeat=1):
            palindrome = ''.join(sorted(perm + combo)) + ''.join(sorted(perm, reverse=True))
            palindromes.add(palindrome)
    return palindromes