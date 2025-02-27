from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:6])).lower()
    counts = Counter(letters)
    mid, halves = ('', [])
    for letter, count in counts.items():
        halves.append(letter * (count // 2))
        if count % 2:
            mid = letter
            break
    palindromes = set()
    for half in set(map(''.join, itertools.permutations(''.join(halves)))):
        palindrome = half + mid + half[::-1]
        if len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes