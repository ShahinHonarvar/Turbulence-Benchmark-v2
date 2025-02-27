import itertools

def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = set(s)
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            permutations = set(itertools.permutations(combination))
            for perm in permutations:
                candidate = ''.join(perm)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes