def return_vowels(string):
    return [char for i, char in enumerate(string) if 24 <= i < 64 and 'F' < char <= 'h' and (char in 'aeiou')]