def palindromes_between_indices(s):
    letters = s[4:6]
    letters = letters.lower()
    letters = ''.join(sorted(letters))
    length = len(letters)
    palindromes = set()
    for i in range(length):
        for j in range(i + 2, length + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes