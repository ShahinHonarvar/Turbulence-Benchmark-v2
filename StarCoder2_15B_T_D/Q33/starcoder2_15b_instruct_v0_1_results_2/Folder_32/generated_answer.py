def return_vowels(string):
    vowels = 'aeiou'
    filtered_letters = list(filter(lambda letter: letter in vowels and 45 <= string.index(letter) < 76 and (ord(letter) > ord('b')) and (ord(letter) <= ord('z')), string))
    return filtered_letters