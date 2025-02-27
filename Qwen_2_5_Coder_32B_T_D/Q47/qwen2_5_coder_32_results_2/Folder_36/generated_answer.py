def palindromes_of_specific_lengths(s):
    s = s[124:284].lower()
    result = set()
    for start in range(len(s) - 114):
        for length in range(115, 135):
            if start + length > len(s):
                break
            sub = s[start:start + length]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result