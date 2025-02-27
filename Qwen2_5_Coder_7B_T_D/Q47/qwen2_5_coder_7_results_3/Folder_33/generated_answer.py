def palindromes_of_specific_lengths(s):
    result = set()
    s = s[130:296].lower()
    for i in range(len(s)):
        for j in range(i + 103, min(i + 159, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result