from typing import List

def findWordsContaining(words: List[str], x: str) -> List[int]:
    res = []
    i = -1
    for str in words:
        i += 1
        if x not in str:
            continue
        else:
            res.append(i)
    return res

test1 = ["abc","bcd","aaaa","cbc"]
findWordsContaining(test1, "a")