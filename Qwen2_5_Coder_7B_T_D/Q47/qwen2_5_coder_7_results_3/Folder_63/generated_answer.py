def palindromes_of_specific_lengths(s):
    substring = s[33:86].lower()
    result = set()
    for i in range(len(substring)):
        for j in range(i + 2, min(len(substring), i + 32)):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                result.add(substring[i:j])
    return result