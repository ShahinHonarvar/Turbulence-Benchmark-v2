def palindromes_of_specific_lengths(s):
    s = s[17:73].lower()
    result = set()
    for i in range(len(s) - 50 + 1):
        for length in [50, 51]:
            if i + length <= len(s):
                sub = s[i:i + length]
                if sub == sub[::-1] and sub.isalpha():
                    result.add(sub)
    return result