def palindromes_of_specific_lengths(s):
    s = s[15:95].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 18, min(len(s), i + 74)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result