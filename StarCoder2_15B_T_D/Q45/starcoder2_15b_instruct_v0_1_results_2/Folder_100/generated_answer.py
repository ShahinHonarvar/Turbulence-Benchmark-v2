def palindromes_between_indices(string):
    letters = sorted(set(string[0:6].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                palindrome = letters[i] + letters[j] + letters[k]
                palindromes.add(palindrome)
                palindromes.add(palindrome[::-1])
    return palindromes