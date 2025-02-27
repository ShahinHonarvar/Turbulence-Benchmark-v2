def palindromes_of_specific_lengths(s):
    s = s[15:96]
    result = set()
    for length in range(20, 67):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                result.add(substring)
    return result