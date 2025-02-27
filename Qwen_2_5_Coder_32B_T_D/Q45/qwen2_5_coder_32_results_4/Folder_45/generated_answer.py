from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = ''.join([c for c in s if c.isalpha()])
    letter_counts = Counter(letters)
    half_palindrome = []
    middle = ''
    for letter, count in letter_counts.items():
        half_palindrome.extend(letter * (count // 2))
        if middle == '' and count % 2 == 1:
            middle = letter
    half_length = len(half_palindrome)
    if half_length < 2:
        return set()
    palindromes = set()
    for half in set(permutations(half_palindrome)):
        half_str = ''.join(half)
        palindrome = half_str + middle + half_str[::-1]
        palindromes.add(palindrome)
    return palindromes