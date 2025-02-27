def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = list(s)
    n = len(letters)
    palindromes = set()
    for length in range(4, n + 1):
        for i in range(n - length + 1):
            substring = ''.join(letters[i:i + length])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes