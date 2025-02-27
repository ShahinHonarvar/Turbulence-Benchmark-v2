def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = list(s)
    n = len(letters)
    result = set()
    for i in range(n):
        for j in range(i + 3, n + 1):
            substring = ''.join(letters[i:j])
            if substring == substring[::-1]:
                result.add(substring)
    return result