def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 20, min(len(s), i + 31)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result