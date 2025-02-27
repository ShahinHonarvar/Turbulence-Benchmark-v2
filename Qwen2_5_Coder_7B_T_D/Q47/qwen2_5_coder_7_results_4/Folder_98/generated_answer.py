def palindromes_of_specific_lengths(s):
    s = s[:21].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 5, min(len(s), i + 81)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result