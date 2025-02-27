def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    substring = s[1:8]
    for i in range(len(substring) - 2):
        if substring[i].isalpha() and substring[i + 2].isalpha():
            if substring[i].lower() == substring[i + 2].lower():
                palindrome_set.add(substring[i:i + 3])
        if substring[i].isalpha() and substring[i + 3].isalpha():
            if substring[i].lower() == substring[i + 3].lower():
                palindrome_set.add(substring[i:i + 4])
    return palindrome_set