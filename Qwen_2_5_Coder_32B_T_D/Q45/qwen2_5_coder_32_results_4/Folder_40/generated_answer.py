from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    counts = Counter(letters)
    if len(letters) < 7:
        return set()
    half_length = (7 + 7 % 2) // 2
    pool = []
    for char, count in counts.items():
        if count // 2 > 0:
            pool.extend(char * (count // 2))
    palindromes = set()
    for perm in permutations(pool, half_length):
        half = ''.join(perm)
        mid = ''
        remaining = ''.join(reversed(perm))
        if 7 % 2 == 1:
            for char, count in counts.items():
                if count % 2 == 1:
                    mid = char
                    break
        palindrome = half + mid + remaining
        palindromes.add(palindrome)
    return palindromes