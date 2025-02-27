def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for i in range(3, 7):
        for j in range(i, 7):
            palindrome = letters[i:j + 1][::-1]
            if palindrome == letters[i:j + 1]:
                palindromes.add(''.join(palindrome))
    return palindromes