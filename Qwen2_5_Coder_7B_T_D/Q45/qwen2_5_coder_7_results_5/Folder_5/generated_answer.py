def palindromes_between_indices(s):
    letters = [char for char in s[4:9] if char.isalpha()]
    letters = [char.lower() for char in letters]
    unique_letters = set(letters)
    if len(unique_letters) < 2:
        return set()
    max_length = len(unique_letters) * 2
    if max_length < 4:
        return set()
    palindromes = set()
    for length in range(4, max_length + 1, 2):
        for perm in itertools.permutations(unique_letters, length):
            half = ''.join(perm)
            full = half + half[::-1]
            if full not in palindromes:
                palindromes.add(full)
    return palindromes