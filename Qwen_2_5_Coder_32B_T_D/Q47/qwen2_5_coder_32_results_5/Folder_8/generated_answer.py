def palindromes_of_specific_lengths(s):
    s = s[17:73].lower()
    result = set()
    for start in range(len(s) - 50 + 1):
        for length in range(50, 52):
            if start + length <= len(s):
                sub = s[start:start + length]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result