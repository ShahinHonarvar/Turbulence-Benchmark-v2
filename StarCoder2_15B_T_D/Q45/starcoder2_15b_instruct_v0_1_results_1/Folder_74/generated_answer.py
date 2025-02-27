def palindromes_between_indices(string):
    letters = sorted(set(string.lower()))
    palindromes = set()
    for i in range(1, len(letters) - 5):
        for j in range(i + 1, len(letters) - 4):
            for k in range(j + 1, len(letters) - 3):
                for l in range(k + 1, len(letters) - 2):
                    for m in range(l + 1, len(letters) - 1):
                        for n in range(m + 1, len(letters)):
                            palindromes.add(letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n])
    return palindromes