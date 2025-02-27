def palindromes_between_indices(string):
    letters = {letter for letter in string if letter.isalpha()}
    palindromes = set()
    for letter in letters:
        palindrome = letter.lower() + letter.lower()[::-1]
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes