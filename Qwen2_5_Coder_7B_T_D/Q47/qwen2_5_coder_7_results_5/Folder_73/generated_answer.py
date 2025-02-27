def palindromes_of_specific_lengths(s):
    result = set()
    s = s[21:63].lower()
    for i in range(len(s)):
        for j in range(i + 22, min(len(s), i + 34)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result