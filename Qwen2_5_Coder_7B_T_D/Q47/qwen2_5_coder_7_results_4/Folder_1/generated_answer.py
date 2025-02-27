def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    substring = s[15:90].lower()
    for i in range(len(substring)):
        for j in range(i + 40, min(j + 73, len(substring) + 1)):
            sub = substring[i:j]
            if is_palindrome(sub) and sub.isalpha():
                result.add(sub)
    return result