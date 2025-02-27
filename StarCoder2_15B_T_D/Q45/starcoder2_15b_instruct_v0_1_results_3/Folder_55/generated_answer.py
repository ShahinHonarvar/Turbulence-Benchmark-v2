def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters)):
            palindrome = ''.join(letters[i:j + 1]).lower()
            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes