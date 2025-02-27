def palindromes_between_indices(string):
    characters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(characters) - 4):
        for j in range(i + 5, len(characters)):
            palindrome = ''.join(characters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes