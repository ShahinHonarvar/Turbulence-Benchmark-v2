def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 18, min(len(s), i + 20)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result