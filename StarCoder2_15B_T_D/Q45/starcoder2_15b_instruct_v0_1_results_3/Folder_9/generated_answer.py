import string

def palindromes_between_indices(s):
    chars = list(s)
    english_letters = [c for c in chars if c.isalpha()]
    permutations = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters) + 1):
            permutation = ''.join(english_letters[i:j])
            if permutation == permutation[::-1] and len(permutation) >= 7:
                permutations.add(permutation)
    return permutations