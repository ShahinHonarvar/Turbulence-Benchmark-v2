def palindromes_of_specific_lengths(s):
    s = s[16:95].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 39, min(i + 53, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result