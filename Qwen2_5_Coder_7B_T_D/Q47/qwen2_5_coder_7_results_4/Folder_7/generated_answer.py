def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[119:257]
    lower_substring = substring.lower()
    for i in range(len(lower_substring) - 122):
        for j in range(104, 124):
            if lower_substring[i:i + j] == lower_substring[i:i + j][::-1] and lower_substring[i:i + j].isalpha():
                result.add(substring[i:i + j])
    return result