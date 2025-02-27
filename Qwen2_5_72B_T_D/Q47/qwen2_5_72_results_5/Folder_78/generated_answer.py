def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[15:73].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 19, min(i + 56, len(s) + 1)):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                result.add(s[i:j])
    return result