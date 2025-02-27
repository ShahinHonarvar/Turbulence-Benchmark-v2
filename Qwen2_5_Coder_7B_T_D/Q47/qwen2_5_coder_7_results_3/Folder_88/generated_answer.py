def palindromes_of_specific_lengths(s):
    result = set()
    s = s[11:88].lower()
    for i in range(len(s) - 3):
        if s[i] == s[i + 4] and s[i + 1] == s[i + 3]:
            result.add(s[i:i + 5])
        if s[i] == s[i + 3]:
            result.add(s[i:i + 4])
    return result