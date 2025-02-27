def return_vowels(string):
    vowels = ['e', 'i', 'o', 'u']
    result = [char for char in string[464:574] if char in vowels and char > 'a' and (char <= 'g')]
    return result