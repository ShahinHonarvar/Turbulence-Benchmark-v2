def palindromes_between_indices(string):
    characters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(1, len(characters) - 1):
        for j in range(i + 1, len(characters)):
            palindrome = characters[i:j + 1][::-1] + characters[i:j]
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes