def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result_set = set()
    s = s[11:94]
    for length in range(34, 55):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                result_set.add(sub.lower())
    return result_set