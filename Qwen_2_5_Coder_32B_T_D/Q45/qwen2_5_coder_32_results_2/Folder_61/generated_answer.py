from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:8])).lower()
    count = Counter(letters)
    half = ''
    middle = ''
    for char, cnt in count.items():
        half += char * (cnt // 2)
        if middle == '' and cnt % 2 == 1:
            middle = char
    palindromes = set()
    for p in permutations(half):
        palindrome = ''.join(p) + middle + ''.join(reversed(p))
        if len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes