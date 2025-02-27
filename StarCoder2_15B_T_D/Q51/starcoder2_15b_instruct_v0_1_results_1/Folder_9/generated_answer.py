def if_contains_anagrams(words):
    anagrams = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if are_anagrams(words[i], words[j]) and are_same_length(words[i], words[j]):
                anagrams.append((words[i], words[j]))
    return len(anagrams) <= 475

def are_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    count1 = {}
    count2 = {}
    for letter in word1:
        count1[letter] = count1.get(letter, 0) + 1
    for letter in word2:
        count2[letter] = count2.get(letter, 0) + 1
    return count1 == count2

def are_same_length(word1, word2):
    return len(word1) == len(word2)