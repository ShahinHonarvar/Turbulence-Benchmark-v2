from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = s[4:9].lower()
    letter_counts = Counter(letters)
    valid_letters = [char for char in letter_counts if char in string.ascii_lowercase]
    if len(valid_letters) < 6:
        return set()
    palindromes = set()
    for perm in permutations(valid_letters, 6):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes