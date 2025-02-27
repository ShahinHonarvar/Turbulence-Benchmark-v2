def palindromes_between_indices(string):
    letters = [letter for letter in string[7:10].lower() if letter.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes