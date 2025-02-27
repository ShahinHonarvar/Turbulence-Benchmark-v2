def palindromes_between_indices(string):
    palindromes = set()
    letters = [letter for letter in string if letter.isalpha()]
    for i in range(len(letters) - 5):
        for j in range(i + 5, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes