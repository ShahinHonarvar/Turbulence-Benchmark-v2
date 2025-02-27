def palindromes_of_specific_lengths(s):
    substring = s[27:78]
    result_set = {s[i:j] for i in range(len(substring)) for j in range(i + 18, i + 19 + 1) if substring[i:j].isalpha() and substring[i:j].lower() == substring[i:j][::-1]}
    return result_set