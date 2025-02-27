def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[62:89].lower()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring) + 1):
            substr = substring[i:j]
            if len(substr) >= 18 and len(substr) <= 21 and (substr == substr[::-1]) and substr.isalpha():
                result.add(substr)
    return result