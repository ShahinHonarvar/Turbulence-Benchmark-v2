def palindromes_of_specific_lengths(s):
    result = set()
    s = s[31:72].lower()
    for length in range(21, 33):
        for start in range(31 - length + 1):
            if s[start:start + length] == s[start:start + length][::-1]:
                result.add(s[start:start + length])
    return result