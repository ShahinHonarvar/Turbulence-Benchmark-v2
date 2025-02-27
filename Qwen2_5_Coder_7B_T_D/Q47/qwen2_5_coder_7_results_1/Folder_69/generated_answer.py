def palindromes_of_specific_lengths(s):
    result = set()
    s = s[11:97].lower()
    for i in range(len(s)):
        for j in range(i + 45, min(i + 53, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result