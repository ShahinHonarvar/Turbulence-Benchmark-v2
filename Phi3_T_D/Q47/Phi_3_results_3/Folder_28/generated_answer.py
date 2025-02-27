def palindromes_of_specific_lengths(s):
    start, end = (32, 72)
    found_palindromes = set()

    def is_palindrome(string):
        return string.lower() == string[::-1].lower()
    for i in range(start, end + 1):
        for length in range(21, 33):
            if i + length <= end:
                if is_palindrome(s[i:i + length]) and all((c.isalpha() for c in s[i:i + length].lower())):
                    found_palindromes.add(s[i:i + length])
    return found_palindromes