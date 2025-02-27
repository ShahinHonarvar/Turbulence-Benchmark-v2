def palindromes_between_indices(s):
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 2):
        for j in range(i + 3, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes