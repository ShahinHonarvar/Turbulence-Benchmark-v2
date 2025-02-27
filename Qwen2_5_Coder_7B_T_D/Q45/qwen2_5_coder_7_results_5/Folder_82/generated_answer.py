def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = set(s)
    result = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = ''.join(sorted(s[i:j + 1]))
            if substring == substring[::-1] and len(substring) >= 7:
                result.add(substring)
    return result