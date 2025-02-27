def palindromes_of_specific_lengths(s):
    s = s[3:301].lower()
    palindromes_set = set()

    def is_english_letter(c):
        return 'a' <= c <= 'z'

    def find_palindromes_around(center, length):
        for offset in range(1, min(length, len(s) - center - (length - 1))):
            substr = s[center - offset:center + offset + 1]
            if substr == substr[::-1]:
                palindromes_set.add(substr.upper())
    for center in range(3, 302):
        for length in range(30, 301):
            if 2 * length <= len(s) - center:
                find_palindromes_around(center, length)
            else:
                break
    return palindromes_set