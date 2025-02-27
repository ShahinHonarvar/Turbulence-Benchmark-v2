def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[464:574] if char in vowels and char > 'a' and (char <= 'g')]