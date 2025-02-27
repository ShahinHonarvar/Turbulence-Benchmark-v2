from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    letter_counts = Counter(letters)
    half = []
    center = ''
    for letter, count in letter_counts.items():
        half.extend(letter * (count // 2))
        if count % 2 == 1 and (not center):
            center = letter
    palindromes = set()
    for half_permutation in set(itertools.permutations(half)):
        half_str = ''.join(half_permutation)
        palindrome = half_str + center + half_str[::-1]
        palindromes.add(palindrome)
    return palindromes