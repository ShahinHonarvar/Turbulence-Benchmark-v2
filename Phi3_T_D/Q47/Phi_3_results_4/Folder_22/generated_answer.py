def palindromes_of_specific_lengths(s):
    start, end = (100, 200)
    substring = s[start:end + 1].lower()

    def is_palindrome(cs, length):
        return cs == cs[::-1] and cs.isalpha()
    return {cs for length in range(5, 11) for i in range(len(substring) - length + 1) if is_palindrome(substring[i:i + length])}