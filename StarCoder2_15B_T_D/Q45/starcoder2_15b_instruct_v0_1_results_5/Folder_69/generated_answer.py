def palindromes_between_indices(string):
    palindromes = set()
    letters = [c for c in string if c.isalpha()]
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes