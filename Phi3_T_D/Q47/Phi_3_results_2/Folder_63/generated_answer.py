def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join(filter(str.isalpha, s[33:86].lower()))
    for length in range(26, 32):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                result.add(s[i:i + length])
    return result