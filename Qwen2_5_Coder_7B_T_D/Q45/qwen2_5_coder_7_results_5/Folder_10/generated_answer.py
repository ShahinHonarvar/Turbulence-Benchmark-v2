from itertools import permutations

def palindromes_between_indices(s):
    letters = s[:6].lower()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(3, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes