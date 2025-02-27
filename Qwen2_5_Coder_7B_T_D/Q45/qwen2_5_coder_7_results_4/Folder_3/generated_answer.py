def palindromes_between_indices(s):
    letters = s[7:10].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            substring = ''.join(sorted(letters[i:j]))
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes