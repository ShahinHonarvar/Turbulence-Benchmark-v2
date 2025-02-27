def palindromes_of_specific_lengths(s):
    result = set()
    s = s[75:96].lower()
    for i in range(len(s)):
        for j in range(i + 7, min(i + 10, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result