def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    specified_substring = s[119:257]
    palindromes_set = set()
    for length in range(104, 124):
        for i in range(len(specified_substring) - length + 1):
            sub = specified_substring[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes_set.add(sub)
    return palindromes_set