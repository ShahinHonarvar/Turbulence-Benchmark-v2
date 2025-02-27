def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    specified_substring = s[12:57]
    palindromes_set = set()
    for length in [20, 21]:
        for i in range(len(specified_substring) - length + 1):
            sub = specified_substring[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes_set.add(sub)
    return palindromes_set