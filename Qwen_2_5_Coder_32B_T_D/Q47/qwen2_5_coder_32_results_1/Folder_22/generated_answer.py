def palindromes_of_specific_lengths(s):
    s = s[100:201].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 5, min(i + 11, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result