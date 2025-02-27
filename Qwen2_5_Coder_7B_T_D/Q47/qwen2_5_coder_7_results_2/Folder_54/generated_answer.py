def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[27:78].lower()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 20, len(substring) + 1)):
            sub = substring[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result