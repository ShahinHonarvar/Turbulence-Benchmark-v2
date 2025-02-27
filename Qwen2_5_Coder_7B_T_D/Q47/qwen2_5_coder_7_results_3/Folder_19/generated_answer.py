def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:56].lower()
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result