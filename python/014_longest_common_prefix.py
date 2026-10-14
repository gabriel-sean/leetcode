import os

def clear_console():
    if os.name == 'nt': os.system('cls') 
    else: os.system('clear')

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        firstword = strs[0]
        for word in strs:
            while not word.startswith(firstword):
                firstword = firstword[:-1]
        return firstword




strs = []
while True:
    print('Enter quit to quit')
    word = str(input('Enter a word: '))
    if word == 'quit': break
    clear_console()
    strs.append(word)

print(strs)
print(Solution().longestCommonPrefix(strs))

