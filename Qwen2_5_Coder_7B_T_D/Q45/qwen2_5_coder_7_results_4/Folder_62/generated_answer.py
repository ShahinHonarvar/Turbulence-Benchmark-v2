def palindromes_between_indices(s):
    letters = s[:9].lower()
    unique_letters = set(letters)
    half_len = 7 // 2
    palindromes = set()
    for i in range(len(letters) - 1, half_len - 2, -1):
        for comb in set(itertools.permutations(letters, i)):
            if comb == comb[::-1] and len(comb) == 7:
                palindromes.add(''.join(comb))
    return palindromes