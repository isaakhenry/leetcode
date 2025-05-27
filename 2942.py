from typing import List

def findWordsContaining(words: List[str], x: str) -> List[int]:
    res = []
    n = len(words)
    for i in range(n):
        if x in words[i]:
           res.append(i)
    return res

test1 = ["abc","bcd","aaaa","cbc"]
findWordsContaining(test1, "a")