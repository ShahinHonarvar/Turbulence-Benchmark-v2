def palindromes_of_specific_lengths(s):
    s = s[125:284]
    s = s.lower()
    result = set()
    for length in range(109, 127):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result