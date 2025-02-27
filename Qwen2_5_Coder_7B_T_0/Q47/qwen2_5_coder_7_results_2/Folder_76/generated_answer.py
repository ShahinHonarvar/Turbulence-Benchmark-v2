def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[101:293].lower()
    for i in range(len(substring)):
        for j in range(i + 154, min(i + 183, len(substring)) + 1):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                result.add(substring[i:j])
    return result