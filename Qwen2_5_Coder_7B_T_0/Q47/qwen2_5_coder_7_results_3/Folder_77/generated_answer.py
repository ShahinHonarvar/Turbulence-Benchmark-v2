def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[103:277].lower()
    for i in range(len(substring)):
        for j in range(i + 100, min(len(substring), i + 170)):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                result.add(substring[i:j])
    return result