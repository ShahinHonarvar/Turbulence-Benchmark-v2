def palindromes_of_specific_lengths(s):
    result = set()
    s = s[17:96].lower()
    for i in range(len(s)):
        for j in range(i + 13, min(len(s), i + 50)):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result