def palindromes_of_specific_lengths(s):
    result = set()
    s = s[103:277].lower()
    for i in range(len(s)):
        for j in range(i + 100, min(len(s), i + 170)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result