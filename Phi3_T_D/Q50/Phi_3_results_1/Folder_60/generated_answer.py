def if_contains_anagrams(words):
    anagrams_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sorted(words[i].lower()) == sorted(words[j].lower()) and len(words[i]) >= 3:
                anagrams_count += 1
                if anagrams_count >= 60:
                    return True
    return False