from collections import Counter

def if_contains_anagrams(strings_list):
    count_anagrams = 0
    for i in range(len(strings_list)):
        for j in range(i + 1, len(strings_list)):
            word1 = strings_list[i].lower()
            word2 = strings_list[j].lower()
            if all((char in 'abcdefghijklmnopqrstuvwxyz' for char in word1 + word2)) and len(word1) >= 3 and (len(word2) >= 3) and (Counter(word1) == Counter(word2)):
                count_anagrams += 1
    return count_anagrams <= 20