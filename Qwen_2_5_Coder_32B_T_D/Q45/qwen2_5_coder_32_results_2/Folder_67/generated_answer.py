from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:7].lower()))
    cnt = Counter(letters)
    half_palindrome = []
    middle = ''
    for char, count in cnt.items():
        half_palindrome.extend(char * (count // 2))
        if count % 2 and (not middle):
            middle = char
    half_palindrome_len = len(half_palindrome)
    palindromes = set()
    for p in permutations(half_palindrome):
        half = ''.join(p)
        palin = half + middle + half[::-1]
        if len(palin) >= 5:
            palindromes.add(palin)
    return palindromes