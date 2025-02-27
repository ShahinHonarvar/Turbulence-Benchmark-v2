def palindromes_between_indices(string):
    palindromes = set()
    letters = [letter for letter in string.lower() if letter.isalpha()]
    for i in range(1, 8):
        for j in range(i + 4, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes