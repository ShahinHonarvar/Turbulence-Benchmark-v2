def palindromes_between_indices(string):
    valid_letters = [c for c in string[6:10].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(valid_letters) - 2):
        for j in range(i + 2, len(valid_letters)):
            palindrome = valid_letters[i:j + 1]
            if len(palindrome) >= 3:
                palindromes.add(''.join(palindrome))
    return palindromes