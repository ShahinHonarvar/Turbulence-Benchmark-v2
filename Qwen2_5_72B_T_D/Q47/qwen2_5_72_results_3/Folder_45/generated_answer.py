def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    specified_substring = s[70:141]
    palindromes = set()
    for length in range(3, 61):
        for i in range(len(specified_substring) - length + 1):
            potential_palindrome = specified_substring[i:i + length]
            if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome.lower())
    return palindromes