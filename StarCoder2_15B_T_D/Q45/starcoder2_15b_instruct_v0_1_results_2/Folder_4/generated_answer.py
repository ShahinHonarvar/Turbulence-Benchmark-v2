def palindromes_between_indices(string):
    characters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(characters) - 6):
        for j in range(i + 6, len(characters)):
            palindrome = ''.join(characters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes