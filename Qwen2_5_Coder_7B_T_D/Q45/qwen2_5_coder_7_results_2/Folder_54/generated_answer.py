def palindromes_between_indices(s):
    letters = s[4:10].lower()
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i + 1, len(unique_letters) + 1):
            for perm in set(permutations(unique_letters[i:j])):
                word = ''.join(perm)
                if word == word[::-1] and len(word) >= 4:
                    palindromes.add(word)
    return palindromes