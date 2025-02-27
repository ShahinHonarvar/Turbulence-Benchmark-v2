def if_contains_anagrams(arr):

    def are_anagrams(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1) == sorted(s2)
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if are_anagrams(arr[i].lower(), arr[j].lower()):
                count += 1
                if count > 94:
                    return False
    return count <= 94