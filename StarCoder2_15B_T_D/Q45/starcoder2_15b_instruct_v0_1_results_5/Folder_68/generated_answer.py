def palindromes_between_indices(string):
    characters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(1, len(characters) - 2):
        for j in range(i + 3, len(characters) + 1):
            for k in range(i, j):
                palindrome = characters[i:k + 1] + characters[k - 1:i - 1:-1]
                if len(palindrome) >= 4:
                    palindromes.add(''.join(palindrome).lower())
    return palindromes