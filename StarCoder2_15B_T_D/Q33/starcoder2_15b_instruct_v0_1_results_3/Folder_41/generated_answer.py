def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[71:81] if char in vowels and char > '>' and (char <= 'U')]