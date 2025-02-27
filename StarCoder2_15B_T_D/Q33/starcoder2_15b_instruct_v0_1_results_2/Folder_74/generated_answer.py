def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [c for c in string[69:82] if c in vowels and '{' < c <= '~']