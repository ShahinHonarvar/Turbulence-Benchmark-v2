def palindromes_of_specific_lengths(s):
    result = set()
    s = s[23:83].lower()
    for length in range(32, 35):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result