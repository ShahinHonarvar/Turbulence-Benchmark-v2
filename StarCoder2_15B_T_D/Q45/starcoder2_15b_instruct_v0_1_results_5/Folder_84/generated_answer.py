def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) - 1):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j]
            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes