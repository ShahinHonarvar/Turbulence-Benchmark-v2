def return_vowels(string):
    vowels = [char for i, char in enumerate(string) if 70 <= i < 76 and char > '2' and (char <= ':') and (char in 'aeiou')]
    return vowels