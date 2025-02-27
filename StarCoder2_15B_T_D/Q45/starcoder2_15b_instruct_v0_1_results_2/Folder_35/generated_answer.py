def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for i in range(2, len(letters) - 1):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i:j + 1][::-1] + letters[i:j + 1]
            if len(palindrome) >= 4 and palindrome.lower() == palindrome:
                palindromes.add(palindrome)
    return palindromes