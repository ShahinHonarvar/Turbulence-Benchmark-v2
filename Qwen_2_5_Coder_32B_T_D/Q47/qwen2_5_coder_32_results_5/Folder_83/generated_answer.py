def palindromes_of_specific_lengths(s):
    s = s[75:96].upper()
    result = set()
    for i in range(len(s) - 6):
        for j in range(i + 7, i + 10):
            sub = s[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result