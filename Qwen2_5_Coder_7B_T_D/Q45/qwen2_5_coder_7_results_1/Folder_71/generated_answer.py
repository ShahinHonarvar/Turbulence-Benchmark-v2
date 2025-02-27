def palindromes_between_indices(s):
    result = set()
    s = s[1:4].lower()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result