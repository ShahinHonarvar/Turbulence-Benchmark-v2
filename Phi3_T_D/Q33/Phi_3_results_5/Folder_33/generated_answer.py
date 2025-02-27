def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E']
    result = [char for char in text[163:771] if ':' < char <= 'E']
    return [char for char in result if char in vowels]