from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:6])).lower()
    counts = Counter(letters)
    mid, half = ('', [])
    for letter, count in counts.items():
        if count % 2:
            mid = letter
            half.append(letter * (count // 2))
        else:
            half.append(letter * (count // 2))
    half = ''.join(half)
    palindromes = set()
    for perm in set(permutations(half)):
        palindrome = ''.join(perm) + mid + ''.join(reversed(perm))
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes