def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(5, 9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 10):
                palindrome = letters[i] + letters[j] + letters[k]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes