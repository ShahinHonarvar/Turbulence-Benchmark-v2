def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    specified_substring = s[10:75]
    valid_palindromes = set()
    for length in range(6, 9):
        for i in range(len(specified_substring) - length + 1):
            substring = specified_substring[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes