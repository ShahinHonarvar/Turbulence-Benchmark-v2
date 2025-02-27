def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters)):
            substring = ''.join(letters[i:j + 1])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes