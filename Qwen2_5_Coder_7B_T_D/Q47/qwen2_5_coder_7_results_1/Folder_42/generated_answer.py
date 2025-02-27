def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[43:96].lower()
    for i in range(len(substring)):
        for j in range(i + 18, min(len(substring), i + 48)):
            sub = substring[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result