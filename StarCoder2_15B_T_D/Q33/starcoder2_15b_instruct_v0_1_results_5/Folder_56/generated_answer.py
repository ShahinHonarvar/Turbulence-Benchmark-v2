def return_vowels(string):
    return [char for i, char in enumerate(string) if i >= 15 and i < 86 and char.isalpha() and (char.lower() in 'aeiou') and ('@' < char <= '~')]