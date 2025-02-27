def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(string)):
        if string[i] in vowels and 82 <= i < 90 and (string[i] > 'T') and (string[i] <= 'b'):
            result.append(string[i])
    return result