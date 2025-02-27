def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    palindromes = set()
    for i in range(5, 10):
        for j in range(i, 10):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes