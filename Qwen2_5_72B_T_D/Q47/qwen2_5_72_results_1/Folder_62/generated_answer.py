def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    specified_substring = s[26:88]
    palindromes = set()
    for i in range(len(specified_substring) - 51):
        for length in range(52, 57):
            substring = specified_substring[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes