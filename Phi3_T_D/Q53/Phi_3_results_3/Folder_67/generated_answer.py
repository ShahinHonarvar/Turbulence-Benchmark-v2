def palindrome_of_length_at_least_n(string):

    def is_english_letter(c):
        return 'a' <= c <= 'z'
    string = string.lower()
    n = 0
    palindromes = set()
    while n <= len(string):
        for j in range(len(string) - n + 1):
            if n >= 25:
                substr = string[j:j + n]
                if substr == substr[::-1] and all((is_english_letter(c) for c in substr)):
                    palindromes.add(substr)
            n += 1
        n = min(n, len(string)) + 1
    return palindromes