def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_chars = [s[i] for i in range(85, 100) if s[i] > '/' and s[i] <= 'n']
    return [char for char in selected_chars if char in vowels]