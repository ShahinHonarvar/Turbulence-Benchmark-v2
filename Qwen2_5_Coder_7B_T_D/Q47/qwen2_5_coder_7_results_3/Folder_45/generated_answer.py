def palindromes_of_specific_lengths(s):
    s = s[70:141].lower()
    result = set()
    for i in range(len(s)):
        for j in range(3, 61):
            if i + j <= len(s) and s[i:i + j] == s[i:i + j][::-1] and s[i:i + j].isalpha():
                result.add(s[i:i + j])
    return result