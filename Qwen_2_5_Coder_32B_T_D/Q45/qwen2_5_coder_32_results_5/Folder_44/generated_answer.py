from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:8])).lower()
    count = Counter(letters)
    half = []
    middle = ''
    for char, freq in count.items():
        half.extend(char * (freq // 2))
        if middle == '' and freq % 2 == 1:
            middle = char
    palindromes = set()
    for perm in itertools.permutations(half):
        half_palindrome = ''.join(perm)
        palindromes.add(half_palindrome + middle + half_palindrome[::-1])
    return {p for p in palindromes if len(p) >= 3}