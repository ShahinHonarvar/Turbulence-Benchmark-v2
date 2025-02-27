def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for i, char in enumerate(string) if 528 <= i < 606 and char in vowels and ('M' < char <= 'X')]