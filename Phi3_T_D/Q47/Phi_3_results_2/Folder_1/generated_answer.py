def palindromes_of_specific_lengths(s):

    def is_english_letter(ch):
        return ch.isalpha() and ch.isascii()

    def find_palindromes(s, min_length, max_length):
        palindromes = set()
        for center in range(min_length - 1, max_length + 1):
            for left in range(center - min_length + 1):
                if (right := (left + 2 * (center - left))):
                    if right > len(s) - 1:
                        break
                    substring = s[left:right + 1]
                    if substring.isalpha() and sum((1 for x, y in zip(substring, substring[::-1]) if x.lower() != y.lower())):
                        continue
                    if is_english_letter(substring[0]) and all((is_english_letter(ch) for ch in substring)):
                        palindromes.add(substring.lower())
        return palindromes
    return find_palindromes(s[15:90], 40, 72)