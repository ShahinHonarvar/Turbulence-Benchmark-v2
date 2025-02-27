def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    specified_substring = s[26:91]
    valid_palindromes = set()
    for start in range(len(specified_substring)):
        for end in range(start + 1, len(specified_substring) + 1):
            if 27 <= end - start <= 58 and specified_substring[start:end].isalpha() and is_palindrome(specified_substring[start:end]):
                valid_palindromes.add(specified_substring[start:end])
    return valid_palindromes