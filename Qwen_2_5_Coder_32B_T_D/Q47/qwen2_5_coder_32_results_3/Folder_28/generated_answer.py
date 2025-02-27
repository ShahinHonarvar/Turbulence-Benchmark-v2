def palindromes_of_specific_lengths(s):
    s = s[32:72].lower()
    result = set()
    for length in range(21, 33):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result