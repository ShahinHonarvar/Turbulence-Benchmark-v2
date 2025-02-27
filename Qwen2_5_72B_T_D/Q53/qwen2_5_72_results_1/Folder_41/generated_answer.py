def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    lower_s = s.lower()
    for i in range(len(lower_s)):
        for j in range(i + 28, len(lower_s) + 1):
            if is_palindrome(lower_s[i:j]):
                if lower_s[i:j].isalpha():
                    palindromes.add(lower_s[i:j])
    return palindromes