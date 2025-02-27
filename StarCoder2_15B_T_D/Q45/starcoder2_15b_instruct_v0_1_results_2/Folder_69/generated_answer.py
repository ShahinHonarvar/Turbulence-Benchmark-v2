def palindromes_between_indices(string):
    characters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(characters) - 3):
        for j in range(i + 3, len(characters)):
            palindrome = ''.join(characters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes