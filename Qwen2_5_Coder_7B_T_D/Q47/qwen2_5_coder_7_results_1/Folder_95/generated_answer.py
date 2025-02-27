def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[12:57].lower()
    for i in range(len(substring)):
        for j in range(i + 2, min(i + 23, len(substring) + 1)):
            sub = substring[i:j]
            if sub == sub[::-1] and sub.isalpha() and (20 <= len(sub) <= 21):
                result.add(sub)
    return result