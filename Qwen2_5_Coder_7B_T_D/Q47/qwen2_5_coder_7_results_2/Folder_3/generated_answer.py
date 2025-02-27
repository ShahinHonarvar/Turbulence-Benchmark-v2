def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[27:96].lower()
    for i in range(len(substring)):
        for j in range(i + 49, i + 52):
            if j <= len(substring):
                if substring[i:j] == substring[i:j][::-1]:
                    result.add(substring[i:j])
    return result