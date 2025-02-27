from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    palindromes = set()
    letter_counts = Counter(letters)
    half_len = 3
    mid = ''
    if any((v & 1 for v in letter_counts.values())):
        odd_letters = [k for k, v in letter_counts.items() if v & 1]
        if len(odd_letters) > 1:
            return palindromes
        mid = odd_letters[0]
        letter_counts[mid] -= 1
    half_palindrome_chars = []
    for letter, count in letter_counts.items():
        half_palindrome_chars.extend([letter] * (count // 2))
    for half in permutations(half_palindrome_chars, half_len):
        half_str = ''.join(half)
        palindromes.add(half_str + mid + half_str[::-1])
    return palindromes