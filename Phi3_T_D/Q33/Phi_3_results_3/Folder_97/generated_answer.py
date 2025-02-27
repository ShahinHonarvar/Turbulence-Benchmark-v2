def return_vowels(s):

    def is_vowel(c):
        return c in 'aeiouAEIOU'
    return [c for c in s[328:455] if is_vowel(c) and c > '']