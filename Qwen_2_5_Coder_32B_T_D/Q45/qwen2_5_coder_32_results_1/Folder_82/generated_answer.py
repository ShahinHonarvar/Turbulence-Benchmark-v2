from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    cnt = Counter(s[1:7].lower())
    valid_chars = ''.join([c * (cnt[c] // 2) for c in letters if cnt[c] > 1])
    mid_chars = ''.join([c for c in letters if cnt[c] % 2 == 1])
    palindromes = set()
    for half in permutations(valid_chars):
        half_str = ''.join(half)
        for mid in mid_chars + ('',):
            palindrome = half_str + mid + half_str[::-1]
            if len(palindrome) >= 7:
                palindromes.add(palindrome)
    return palindromes