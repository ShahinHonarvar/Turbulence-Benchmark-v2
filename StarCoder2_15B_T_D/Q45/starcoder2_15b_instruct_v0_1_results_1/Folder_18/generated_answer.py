def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 1):
        for j in range(i + 1, min(i + 7, len(letters))):
            palindrome = ''.join(letters[i:j])
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes