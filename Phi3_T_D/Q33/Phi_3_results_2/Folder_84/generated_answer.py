def return_vowels(input_string):
    vowels = 'aeiou'
    result = [char for char in input_string[770:852] if char in vowels and ord(char) > ord('B') and (ord(char) <= ord('i'))]
    return result