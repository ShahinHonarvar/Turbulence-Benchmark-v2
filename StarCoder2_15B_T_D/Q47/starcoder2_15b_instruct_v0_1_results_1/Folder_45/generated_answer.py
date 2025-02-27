def palindromes_of_specific_lengths(string):
    palindromes = set()
    lowercase_string = string.lower()
    substring = lowercase_string[70:141]
    for length in range(3, 61):
        for start in range(len(substring) - length + 1):
            substring_palindrome = substring[start:start + length]
            if substring_palindrome == substring_palindrome[::-1]:
                palindromes.add(substring_palindrome)
    return palindromes