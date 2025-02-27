def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    found_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 66, len(s)):
            if is_palindrome(s[i:j + 1]):
                found_palindromes.add(s[i:j + 1])
    return found_palindromes