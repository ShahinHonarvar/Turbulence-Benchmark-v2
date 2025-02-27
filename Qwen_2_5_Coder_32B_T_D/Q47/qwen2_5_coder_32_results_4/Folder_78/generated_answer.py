def palindromes_of_specific_lengths(s):
    s = s[15:73].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 19, min(i + 56, len(s) + 1)):
            sub = s[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result