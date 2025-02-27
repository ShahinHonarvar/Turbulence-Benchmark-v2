def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[15:87].lower()
    for i in range(len(substring)):
        for j in range(i + 51, min(len(substring), i + 61)):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                result.add(substring[i:j])
    return result