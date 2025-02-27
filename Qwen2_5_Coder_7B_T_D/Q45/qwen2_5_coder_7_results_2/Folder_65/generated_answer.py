def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    result = set()
    for i in range(len(letters) - 4):
        for j in range(i + 5, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result