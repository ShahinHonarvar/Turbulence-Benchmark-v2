def return_vowels(text):
    vowels = 'AEIOUaeiou'
    result = [char for char in text[837:975] if char.upper() >= 'N' and char.upper() <= 'W' and (char in vowels)]
    return result