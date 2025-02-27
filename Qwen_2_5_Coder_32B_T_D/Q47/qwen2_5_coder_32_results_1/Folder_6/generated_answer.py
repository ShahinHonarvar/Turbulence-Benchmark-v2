def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    result = set()
    for length in range(40, 48):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result