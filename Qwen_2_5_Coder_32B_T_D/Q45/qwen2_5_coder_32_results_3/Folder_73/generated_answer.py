from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[3:7].lower()
    counts = Counter(sub_s)
    letters = ''.join([c * (counts[c] // 2) for c in counts if counts[c] >= 2])
    odd_chars = [c for c in counts if counts[c] % 2 == 1]
    palindromes = set()
    for mid in odd_chars + ['']:
        for perm in permutations(letters):
            half = ''.join(perm)
            palindrome = half + mid + half[::-1]
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes