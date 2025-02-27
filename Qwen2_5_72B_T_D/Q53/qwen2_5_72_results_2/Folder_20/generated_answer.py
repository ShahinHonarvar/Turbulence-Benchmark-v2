def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = s.lower()
    length = len(s)
    found_palindromes = set()
    for i in range(length):
        for j in range(i + 66, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes