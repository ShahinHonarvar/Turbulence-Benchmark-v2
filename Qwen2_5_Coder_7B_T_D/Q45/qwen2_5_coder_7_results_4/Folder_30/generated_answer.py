def palindromes_between_indices(s):
    s = s[:5].lower()
    letters = sorted(s)
    result = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = ''.join(letters[i:j + 1])
            if len(substring) >= 4 and substring == substring[::-1]:
                result.add(substring)
    return result