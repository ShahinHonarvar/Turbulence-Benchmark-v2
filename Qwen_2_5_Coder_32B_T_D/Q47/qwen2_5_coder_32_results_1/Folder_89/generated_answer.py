def palindromes_of_specific_lengths(s):
    s = s[18:89].lower()
    result = set()
    for i in range(len(s) - 11):
        for length in range(12, 15):
            if i + length <= len(s):
                sub = s[i:i + length]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result