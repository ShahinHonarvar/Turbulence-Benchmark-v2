def palindromes_of_specific_lengths(s):
    result = set()
    s = s[100:301].lower()
    for i in range(len(s)):
        for j in range(i + 50, min(len(s), i + 101)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result