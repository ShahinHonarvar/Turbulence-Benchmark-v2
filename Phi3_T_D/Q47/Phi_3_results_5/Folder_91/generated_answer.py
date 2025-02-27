def palindromes_of_specific_lengths(text):

    def is_english_letter(c):
        return 'a' <= c <= 'z'

    def expand_around_center(s, l, r):
        while l >= 0 and r < len(s) and is_english_letter(s[l]) and is_english_letter(s[r]):
            l -= 1
            r += 1
        if l >= 0 and r < len(s):
            return s[l + 1:r]
        return None
    palindromes = set()
    for center in range(9):
        substr_left = text[0:center:2] if center % 2 == 0 else text[0:center + 1:2]
        substr_right = text[center + 2:11:2] if center % 2 == 0 else text[center + 1:11:2]
        substr = substr_left + substr_right
        for length in range(3, 6):
            for i in range(len(substr) - length + 1):
                possible_palindrome = substr[i:i + length]
                if possible_palindrome.lower() == possible_palindrome.lower()[::-1]:
                    palindromes.add(possible_palindrome.lower())
    return palindromes