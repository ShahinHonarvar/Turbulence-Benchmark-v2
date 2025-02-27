import itertools

def palindromes_between_indices(s):
    segment = s[4:10].lower()
    letters = ''.join(filter(str.isalpha, segment))
    found_palindromes = set()
    for permutation in itertools.permutations(letters, len(letters)):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1] and len(candidate) >= 7:
            found_palindromes.add(candidate)
    return found_palindromes