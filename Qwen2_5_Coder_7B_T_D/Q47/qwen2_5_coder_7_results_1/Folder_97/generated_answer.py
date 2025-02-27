def palindromes_of_specific_lengths(s):
    res = set()
    s = s[28:95].lower()
    for i in range(len(s)):
        for j in range(i + 38, min(i + 50, len(s)) + 1):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                res.add(s[i:j])
    return res