def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    result = set()
    for start in range(len(s) - 135):
        for end in range(start + 135, min(start + 160, len(s)) + 1):
            sub = s[start:end]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result