from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x.lower() in string.ascii_lowercase, s[4:10])).lower()
    count = Counter(letters)
    if len(letters) < 7:
        return set()
    half_length = 7 // 2
    middle = ''
    half = []
    for letter in count:
        if count[letter] % 2 == 1:
            if middle == '':
                middle = letter
            else:
                return set()
        half.extend([letter] * (count[letter] // 2))
    if len(half) < half_length:
        return set()
    res = set()
    for p in permutations(half, half_length):
        half_palindrome = ''.join(p)
        res.add(half_palindrome + middle + half_palindrome[::-1])
    return res