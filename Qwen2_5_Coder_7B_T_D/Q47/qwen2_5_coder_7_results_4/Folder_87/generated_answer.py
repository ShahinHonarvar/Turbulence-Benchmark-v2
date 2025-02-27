def palindromes_of_specific_lengths(s):
    s = s[11:94].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 34, min(i + 55, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result