def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:95].lower()
    for i in range(len(substring)):
        for j in range(i + 39, min(len(substring), i + 53)):
            if substring[i:j + 1] == substring[i:j + 1][::-1]:
                result.add(substring[i:j + 1])
    return result