def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    substring = s[12:93]
    for length in range(17, 67):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].isalpha() and substring[i:i + length] == substring[i:i + length][::-1]:
                result.add(substring[i:i + length])
    return result