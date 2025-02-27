from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(substring)
    odd_counts = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    center = odd_counts[0] if odd_counts else ''
    half_palindrome = ''.join((char * (count // 2) for char, count in letter_counts.items()))
    half_permutations = set([''.join(p) for p in set(permutations(half_palindrome))])
    palindromes = set((p + center + p[::-1] for p in half_permutations if len(p + center + p[::-1]) >= 3))
    return palindromes