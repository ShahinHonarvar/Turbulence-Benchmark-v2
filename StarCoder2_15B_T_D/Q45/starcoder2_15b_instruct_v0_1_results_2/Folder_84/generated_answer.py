def palindromes_between_indices(string):
    letters = sorted(set(string[4:10].lower()))
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters) - 1):
            for k in range(j + 1, len(letters)):
                palindromes.add(letters[i] + letters[j] + letters[k])
                palindromes.add(letters[k] + letters[j] + letters[i])
                palindromes.add(letters[k] + letters[i] + letters[j])
                palindromes.add(letters[j] + letters[k] + letters[i])
                palindromes.add(letters[j] + letters[i] + letters[k])
                palindromes.add(letters[i] + letters[k] + letters[j])
    return palindromes