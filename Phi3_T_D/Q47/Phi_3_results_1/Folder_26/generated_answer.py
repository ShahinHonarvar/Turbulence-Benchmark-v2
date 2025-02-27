def palindromes_of_specific_lengths(s):
    result = set()
    s = s[24:85]
    for length in range(21, 32):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if len(''.join(filter(str.isalpha, substring))) == length and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result