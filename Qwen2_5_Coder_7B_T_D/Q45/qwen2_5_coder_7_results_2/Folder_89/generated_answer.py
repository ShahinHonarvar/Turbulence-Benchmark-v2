def palindromes_between_indices(s):
    indices = s[5:10].lower()
    letters = list(indices)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring == substring[::-1] and len(substring) >= 6:
                palindromes.add(substring)
    return palindromes