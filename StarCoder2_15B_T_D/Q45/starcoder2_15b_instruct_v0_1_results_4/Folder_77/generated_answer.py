def palindromes_between_indices(string):
    letters = [letter for letter in string[4:7].lower() if letter.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindrome = letters[i:j + 1] + letters[j:i:-1]
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes