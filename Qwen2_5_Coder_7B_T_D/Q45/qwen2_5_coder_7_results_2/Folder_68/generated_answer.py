def palindromes_between_indices(s):
    letters = s[1:9].lower()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(4, len(unique_letters) + 1):
        for perm in set(permutations(unique_letters, length)):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes