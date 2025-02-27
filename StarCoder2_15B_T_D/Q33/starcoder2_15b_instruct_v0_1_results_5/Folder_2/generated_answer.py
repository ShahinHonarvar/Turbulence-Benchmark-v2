def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(string) if 170 <= i < 645 and c in vowels and (c > 'E') and (c <= '~')]