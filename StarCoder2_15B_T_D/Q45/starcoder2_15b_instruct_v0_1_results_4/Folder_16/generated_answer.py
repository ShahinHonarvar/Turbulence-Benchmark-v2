def palindromes_between_indices(string):
    palindromes = set()
    letters = [letter for letter in string[6:10].lower() if letter.isalpha()]
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            palindrome = ''.join(letters[i:i + length])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes