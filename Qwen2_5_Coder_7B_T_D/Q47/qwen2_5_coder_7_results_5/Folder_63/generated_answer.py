def palindromes_of_specific_lengths(s):
    result = set()
    s = s[33:86].lower()
    for start in range(len(s)):
        for length in range(26, 32):
            end = start + length
            if end <= len(s) and s[start:end] == s[start:end][::-1] and s[start:end].isalpha():
                result.add(s[start:end])
    return result