def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    palindromes = set()
    for i in range(1, 9):
        for j in range(i + 1, 10):
            palindrome = ''.join(letters[i:j])
            if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes