def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = sorted(s)
    n = len(letters)
    result = set()
    for i in range(n - 6):
        for j in range(i + 6, n + 1):
            substring = ''.join(letters[i:j])
            half_len = (j - i) // 2
            if substring[:half_len] == substring[half_len:][::-1]:
                result.add(substring)
    return result