def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 6):
        for j in range(i + 4, len(letters) - 1):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome.lower() == palindrome[::-1].lower():
                palindromes.add(palindrome)
    return palindromes