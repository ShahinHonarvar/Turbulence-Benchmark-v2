def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 5, len(letters)):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes