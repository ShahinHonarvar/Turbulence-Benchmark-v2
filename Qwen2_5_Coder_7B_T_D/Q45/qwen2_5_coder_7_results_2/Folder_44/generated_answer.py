import itertools

def palindromes_between_indices(s: str) -> set:
    letters = s[2:8].lower()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            candidate = ''.join(combination)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes