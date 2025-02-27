def palindromes_of_specific_lengths(s):
    s = s[39:95].lower()
    result = set()
    for length in range(14, 53):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result