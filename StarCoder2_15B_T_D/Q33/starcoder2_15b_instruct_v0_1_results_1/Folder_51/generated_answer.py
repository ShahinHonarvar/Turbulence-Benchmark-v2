def return_vowels(string):
    return [char for i, char in enumerate(string) if 56 <= i < 68 and char.isalpha() and (char.lower() not in 'aeiou')]