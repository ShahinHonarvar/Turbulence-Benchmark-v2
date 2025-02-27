def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        range_start = max(i - 8, 0)
        range_end = min(i + 1, len(s) - 8)
        for j in range(range_start, range_end + 1):
            substring = s[j:i + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes