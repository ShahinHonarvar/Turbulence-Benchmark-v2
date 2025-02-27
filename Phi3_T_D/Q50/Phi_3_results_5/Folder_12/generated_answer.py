def if_contains_anagrams(words):
    count_anagrams = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sorted(words[i].lower()) == sorted(words[j].lower()) and len(words[i]) >= 3 and (len(words[j]) >= 3):
                count_anagrams += 1
                if count_anagrams >= 69:
                    return True
    return False