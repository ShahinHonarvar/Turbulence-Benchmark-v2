def return_vowels(input_string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for i in range(41, 50):
        char = input_string[i]
        if 'W' < char <= '[' and char in vowels:
            vowel_list.append(char)
    return vowel_list