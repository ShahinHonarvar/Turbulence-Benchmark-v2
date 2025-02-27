def palindromes_between_indices(s):
    letters = s[2:6].lower()
    letters = ''.join(filter(str.isalpha, letters))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes