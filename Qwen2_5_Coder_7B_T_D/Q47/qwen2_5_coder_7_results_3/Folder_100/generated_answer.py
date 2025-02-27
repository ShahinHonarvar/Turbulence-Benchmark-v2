def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[29:97]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 12, min(len(substring), i + 19)):
            if substring[i:j] == substring[i:j][::-1]:
                result.add(substring[i:j])
    return result