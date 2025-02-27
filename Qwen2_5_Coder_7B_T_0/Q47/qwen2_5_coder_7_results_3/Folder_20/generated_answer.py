def palindromes_of_specific_lengths(s):
    s = s[20:75].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 36, min(i + 43, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result