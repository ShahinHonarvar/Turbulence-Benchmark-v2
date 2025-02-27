def palindromes_of_specific_lengths(s):
    result = set()
    for start in range(16, 61):
        for length in range(16, 40):
            end = start + length
            if end <= 61:
                sub = s[start:end].lower()
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result