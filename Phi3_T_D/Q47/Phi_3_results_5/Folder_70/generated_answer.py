def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:71]
    for length in range(24, 53):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length].lower()
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result