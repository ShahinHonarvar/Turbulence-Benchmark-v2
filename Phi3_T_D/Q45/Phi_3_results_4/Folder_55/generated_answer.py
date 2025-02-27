from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(chars):
        length = len(chars)
        if length < 3:
            return []
        perms = set(permutations(chars))
        palindromes = [''.join(p) for p in perms if ''.join(p).lower() == ''.join(p)[::-1].lower()]
        return set(palindromes)
    range_s = s[:3].lower()
    palindromes_set = generate_palindromes(range_s)
    return palindromes_set