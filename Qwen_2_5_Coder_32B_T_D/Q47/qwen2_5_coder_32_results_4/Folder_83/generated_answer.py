def palindromes_of_specific_lengths(s):
    s = s[75:96].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 7, i + 10):
            if j > len(s):
                break
            sub = s[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result