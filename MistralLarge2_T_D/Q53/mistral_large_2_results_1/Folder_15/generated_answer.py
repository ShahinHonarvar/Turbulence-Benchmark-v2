def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub_s):
        return sub_s == sub_s[::-1]
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 4, n + 1):
            sub_s = s[i:j]
            if is_palindrome(sub_s.lower()) and sub_s.isalpha():
                palindromes.add(sub_s)
    return palindromes