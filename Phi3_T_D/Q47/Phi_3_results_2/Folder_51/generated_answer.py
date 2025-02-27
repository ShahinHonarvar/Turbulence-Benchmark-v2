from string import ascii_letters

def palindromes_of_specific_lengths(s):

    def is_english_letter(ch):
        return ch in ascii_letters
    s = s[2:8].lower()
    palindromes = {s[start:start + length] for length in range(3, 5) for start in range(len(s) - length + 1) if all((is_english_letter(ch) for ch in s[start:start + length])) and s[start:start + length] == s[start:start + length][::-1]}
    return palindromes