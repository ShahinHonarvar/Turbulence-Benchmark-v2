def return_vowels(string):
    vowels = [char for char in string[85:99] if char.isalpha() and char.lower() in 'aeiou']
    return sorted(vowels)