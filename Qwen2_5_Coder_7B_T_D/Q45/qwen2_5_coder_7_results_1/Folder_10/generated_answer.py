def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes