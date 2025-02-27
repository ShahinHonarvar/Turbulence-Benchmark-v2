def palindromes_between_indices(s):
    letters = s[4:10]
    letters = ''.join(filter(str.isalpha, letters))
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(6, len(unique_letters) + 1):
        for perm in itertools.permutations(unique_letters, length):
            half = ''.join(perm)
            full = half + half[::-1]
            if half.lower() in letters:
                palindromes.add(full)
    return palindromes