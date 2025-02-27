from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    s = s[:9].lower()
    letters = [c for c in s if c.isalpha()]
    count = Counter(letters)
    valid_half = []
    for c in count:
        if count[c] >= 4:
            valid_half.append(c * 2)
        elif count[c] >= 2:
            valid_half.append(c)
    half_length = len(''.join(valid_half))
    palindromes = set()
    if half_length >= 3:
        for perm in permutations(''.join(valid_half), half_length):
            half = ''.join(perm)
            middle = ''
            if half_length % 2 == 1:
                for c in count:
                    if count[c] % 2 == 1:
                        middle = c
                        break
            palindrome = half + middle + half[::-1]
            if len(palindrome) >= 7:
                palindromes.add(palindrome)
    return palindromes