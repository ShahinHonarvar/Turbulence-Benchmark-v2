def palindromes_between_indices(s):
    substring = s[5:8].lower()
    letters = set(substring)
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in set(itertools.permutations(letters, length)):
            candidate = ''.join(combination)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes