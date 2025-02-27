def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    specified_substring = s[11:97]
    palindromes = set()
    for length in range(45, 53):
        for i in range(len(specified_substring) - length + 1):
            sub = specified_substring[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes