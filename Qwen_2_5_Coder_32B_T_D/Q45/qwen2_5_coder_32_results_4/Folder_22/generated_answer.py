import itertools
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[5:7].lower()))
    unique_chars = set(letters)
    counts = Counter(letters)
    palindromes = set()
    for r in range(3, len(letters) + 1, 2):
        for comb in itertools.combinations_with_replacement(unique_chars, (r + 1) // 2):
            half = ''.join(comb)
            if all((2 * counts[c] >= half.count(c) for c in half)):
                mid = '' if r % 2 == 0 else half[-1]
                half_palindrome = half[:-1] + mid + half[-2::-1]
                palindromes.add(half_palindrome)
    return palindromes