def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[155:284].lower()
    for i in range(len(substring)):
        for j in range(i + 104, min(i + 121, len(substring) + 1)):
            substr = substring[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result