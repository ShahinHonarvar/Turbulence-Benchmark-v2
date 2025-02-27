from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[7:10].lower()))
    counter = Counter(letters)
    half = []
    middle = ''
    for char, count in counter.items():
        half.append(char * (count // 2))
        if count % 2 and (not middle):
            middle = char
    half = ''.join(half)
    palindromes = set()
    for perm in set(itertools.permutations(half)):
        palindrome = ''.join(perm) + middle + ''.join(reversed(perm))
        if len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes