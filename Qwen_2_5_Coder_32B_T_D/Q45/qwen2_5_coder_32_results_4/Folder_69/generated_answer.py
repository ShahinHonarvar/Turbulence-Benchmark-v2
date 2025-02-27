from itertools import permutations
    from collections import Counter
    import string

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:4])).lower()
    if len(letters) < 4:
        return set()
    letter_count = Counter(letters)
    half_length = len(letters) // 2
    half_palindrome = []
    mid = ''
    for char, count in letter_count.items():
        half_palindrome.extend(char * (count // 2))
        if count % 2 == 1 and (len(letters) % 2 == 1 or mid == ''):
            mid = char
    half_palindrome = ''.join(sorted(half_palindrome))
    palindromes = set()
    for perm in permutations(half_palindrome):
        half = ''.join(perm)
        palindrome = half + mid + half[::-1]
        palindromes.add(palindrome)
    return palindromes