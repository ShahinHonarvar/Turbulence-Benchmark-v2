def palindromes_of_specific_lengths(s):
    substring = s[30:91]
    valid_palindromes = {palindrome for palindrome in [substring[i:j + 1] for i in range(len(substring)) for j in range(i, len(substring)) if len(substring[i:j + 1]) in range(50, 54) and substring[i:j + 1].isalpha() and (substring[i:j + 1].lower() == substring[i:j + 1][::-1].lower())]}
    return valid_palindromes