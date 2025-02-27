def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    result_set = set()
    substring = s[1:8]
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].isalpha():
                if is_palindrome(substring[i:i + length]):
                    result_set.add(substring[i:i + length])
    return result_set