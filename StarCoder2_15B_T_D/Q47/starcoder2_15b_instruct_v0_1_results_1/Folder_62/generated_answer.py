def palindromes_of_specific_lengths(string):
    substring = string[26:88]
    result = set()
    for length in range(52, 57):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result