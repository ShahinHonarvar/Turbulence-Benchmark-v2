def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[103:277].lower()
    for i in range(len(substring)):
        for j in range(i + 100, min(len(substring), i + 170)):
            sub = substring[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result