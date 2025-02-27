def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[119:257].lower()
    for i in range(len(substring)):
        for j in range(i + 104, min(i + 124, len(substring) + 1)):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                result.add(substring[i:j])
    return result