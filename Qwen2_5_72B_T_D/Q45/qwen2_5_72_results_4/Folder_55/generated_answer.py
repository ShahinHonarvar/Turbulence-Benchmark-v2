from itertools import permutations

def palindromes_between_indices(s):
    substr = s[0:3].lower()
    letter_counts = {}
    for char in substr:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    letters = ''.join([char * count for char, count in letter_counts.items()])
    perms = set([''.join(p) for p in permutations(letters)])
    palindromes = {perm for perm in perms if len(perm) >= 3 and perm == perm[::-1]}
    return palindromes