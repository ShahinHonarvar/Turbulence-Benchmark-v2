def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    specified_substring = s[10:75]
    valid_palindromes = set()
    for length in range(6, 9):
        for start in range(len(specified_substring) - length + 1):
            candidate = specified_substring[start:start + length]
            if is_palindrome(candidate) and candidate.isalpha():
                valid_palindromes.add(candidate.lower())
    return valid_palindromes