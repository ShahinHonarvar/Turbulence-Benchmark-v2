def palindromes_of_specific_lengths(s):
    result = set()
    s = s[2:9].lower()
    for i in range(len(s) - 2):
        for j in range(i + 3, min(i + 5, len(s)) + 1):
            sub = s[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result