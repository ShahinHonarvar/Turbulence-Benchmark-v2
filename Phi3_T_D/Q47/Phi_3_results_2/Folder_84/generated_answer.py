def palindromes_of_specific_lengths(s):
    sub_str = s[23:78]
    lower_limit, upper_limit = (13, 40)
    palindromes = set()
    for length in range(lower_limit, upper_limit + 1):
        for start in range(len(sub_str) - length + 1):
            end = start + length
            substring = sub_str[start:end]
            if substring.isalpha() and substring.casefold() == substring[::-1].casefold():
                palindromes.add(substring)
    palindromes_result = {palindrome for palindrome in palindromes}
    return palindromes_result