def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    specified_substring = s[26:88]
    palindromes = set()
    for i in range(len(specified_substring)):
        for j in range(i + 52, min(i + 57, len(specified_substring) + 1)):
            substring = specified_substring[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes