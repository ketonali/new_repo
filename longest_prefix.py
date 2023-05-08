
def longestCommonPrefix(strs:list):
    min_word = (min(strs, key=len))
    ind, count = 0,0
    prefix = ''
    while ind < len(min_word):
        for word in strs:
            if word[ind] == min_word[ind]:
                count += 1

                if count % len(strs) == 0:
                    prefix += min_word[ind]
                    ind += 1
            else:
                ind = len(min_word)
                break
    return prefix