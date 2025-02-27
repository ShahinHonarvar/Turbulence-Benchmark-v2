def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = sorted(s)
    length = len(letters)
    result = set()
    for i in range(length):
        for j in range(i, length):
            substring = ''.join(letters[i:j + 1])
            if len(substring) >= 7:
                if substring == substring[::-1]:
                    result.add(substring)
    return result