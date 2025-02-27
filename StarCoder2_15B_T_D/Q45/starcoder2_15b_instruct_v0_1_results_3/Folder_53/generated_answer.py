def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(4, 8):
        for j in range(i + 1, 8):
            for k in range(j + 1, 8):
                for l in range(k + 1, 8):
                    for m in range(l + 1, 8):
                        for n in range(m + 1, 8):
                            palindrome = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]
                            palindromes.add(palindrome)
    return palindromes