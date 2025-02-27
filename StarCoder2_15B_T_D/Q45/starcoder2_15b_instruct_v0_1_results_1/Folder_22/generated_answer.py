def palindromes_between_indices(string):
    letters = [c for c in string[5:7].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindrome = letters[i:j + 1] + letters[j:i:-1]
            if len(palindrome) >= 3:
                palindromes.add(''.join(palindrome))
    return palindromes