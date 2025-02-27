def palindromes_between_indices(string):
    letters = [letter for letter in string[3:6].lower() if letter.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                palindrome = letters[i] + letters[j] + letters[k]
                if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes