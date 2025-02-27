def return_vowels(s):
    vowels = ['e', 'i', 'o', 'u']
    return [char for char in s[464:574] if char in vowels and char > 'a' and (char <= 'g')]