def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    substring = s[2:9]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 5, len(substring) + 1)):
            if substring[i:j] == substring[i:j][::-1]:
                result.add(substring[i:j])
    return result