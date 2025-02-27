def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    found_palindromes = set()

    def is_palindrome(sub_s):
        return sub_s == sub_s[::-1]
    for i in range(n):
        for j in range(i + 37, n + 1):
            sub_s = s[i:j]
            if sub_s.isalpha() and is_palindrome(sub_s):
                found_palindromes.add(sub_s)
    return found_palindromes