from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    letters = ''.join(filter(lambda x: x.isalpha(), substring))
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 3:
            palindromes.add(candidate)
    return palindromes