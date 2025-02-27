def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for i in range(3, 9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 10):
                palindrome = letters[i] + letters[j] + letters[k]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes