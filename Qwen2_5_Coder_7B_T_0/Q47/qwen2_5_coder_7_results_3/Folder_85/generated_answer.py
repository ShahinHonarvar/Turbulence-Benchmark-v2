def palindromes_of_specific_lengths(s):
    result = set()
    s = s[29:99].lower()
    for length in range(6, 10):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result