def palindromes_of_specific_lengths(s):
    result = set()
    s = s[125:284].lower()
    for i in range(len(s) - 108):
        for j in range(109, 127):
            if s[i:i + j] == s[i:i + j][::-1] and s[i:i + j].isalpha():
                result.add(s[i:i + j])
    return result