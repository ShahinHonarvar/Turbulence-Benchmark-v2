def palindromes_of_specific_lengths(s):
    s = s[20:75].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 3, i + 43):
            if j <= len(s) and s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result