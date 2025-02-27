def palindromes_between_indices(s):
    result = set()
    for i in range(4, len(s)):
        for j in range(i, len(s)):
            substring = s[j - i + 1:j + 1]
            if len(substring) == i and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result