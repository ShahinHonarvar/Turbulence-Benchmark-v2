def palindromes_of_specific_lengths(s):
    result = set()
    s = s[29:97].lower()
    for i in range(len(s)):
        for j in range(i + 12, min(len(s), i + 19)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result