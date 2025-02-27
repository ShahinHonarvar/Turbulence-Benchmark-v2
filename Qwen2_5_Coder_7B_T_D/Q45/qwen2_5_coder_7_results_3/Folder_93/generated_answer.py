def palindromes_between_indices(s):
    letters = s[2:8].lower()
    unique_letters = set(letters)
    result = set()
    for i in range(len(letters)):
        for j in range(i + 6, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(''.join(sorted(substring)))
    return result