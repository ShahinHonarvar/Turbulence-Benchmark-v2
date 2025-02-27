def palindromes_of_specific_lengths(s):
    start, end = (62, 88)
    sub_str = s[start:end + 1].lower()

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    for length in range(18, 22):
        for i in range(0, end - length + 1):
            if is_palindrome(sub_str[i:i + length]) and sub_str[i:i + length].isalpha():
                palindromes.add(sub_str[i:i + length].upper())
    return palindromes