def palindromes_of_specific_lengths(s):

    def is_palindrome(x, l):
        return x[:l] == x[:l][::-1]

    def only_letters():
        return all((c.isalpha() for c in x))
    s = s[:101].lower()
    return {s[i:i + l] for i in range(101 - l + 1) for l in range(3, 16) if is_palindrome(s[i:], l) and only_letters()}