def palindromes_between_indices(s):
    letters = s[:4].lower()
    unique_letters = set(letters)
    result = set()
    for length in range(4, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            if perm == perm[::-1]:
                result.add(''.join(perm))
    return result