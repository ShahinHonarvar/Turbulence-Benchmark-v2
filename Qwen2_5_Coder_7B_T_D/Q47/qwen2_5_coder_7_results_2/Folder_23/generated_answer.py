def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[23:95].lower()
    for i in range(len(substring)):
        for j in range(i + 17, min(i + 56, len(substring) + 1)):
            sub = substring[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result