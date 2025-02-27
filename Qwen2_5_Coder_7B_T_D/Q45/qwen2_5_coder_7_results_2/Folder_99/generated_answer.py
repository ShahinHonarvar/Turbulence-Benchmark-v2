def palindromes_between_indices(s):
    letters = s[4:9]
    letters = letters.lower()
    letters = ''.join(filter(str.isalpha, letters))
    length = len(letters)
    if length < 3:
        return set()
    palindromes = set()
    for i in range(length):
        for j in range(i + 3, length + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes