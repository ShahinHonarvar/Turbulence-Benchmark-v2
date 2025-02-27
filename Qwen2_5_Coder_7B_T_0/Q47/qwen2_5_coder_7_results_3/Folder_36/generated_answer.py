def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[124:284].lower()
    for i in range(len(substring)):
        for j in range(i + 115, min(i + 135, len(substring) + 1)):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                result.add(substring[i:j])
    return result