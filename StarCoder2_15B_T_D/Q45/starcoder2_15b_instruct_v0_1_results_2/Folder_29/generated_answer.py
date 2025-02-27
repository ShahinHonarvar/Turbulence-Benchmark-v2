def palindromes_between_indices(string):
    letters = sorted(set(string[2:10].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindromes.add(letters[i] + letters[j])
    return palindromes