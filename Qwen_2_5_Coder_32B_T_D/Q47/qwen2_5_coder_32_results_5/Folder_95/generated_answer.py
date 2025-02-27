def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    result = set()
    for i in range(len(s) - 19):
        for l in range(20, 22):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result