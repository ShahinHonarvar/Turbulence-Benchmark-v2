def return_vowels(text):
    vowels = 'AEIOUaeiou'
    result = [char for char in text[17:65] if char in vowels and 'U' < char <= '{']
    return result