def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(6, 10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                for l in range(k + 1, 10):
                    palindrome = ''.join([letters[i], letters[j], letters[k], letters[l]])
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes