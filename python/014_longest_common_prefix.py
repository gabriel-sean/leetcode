'''
14. Longest Common Prefix [Easy]
https://leetcode.com/problems/longest-common-prefix/
O(n x m) time, O(1) space; horizontal scanning
n = number of strings, m = length of shortest string
'''


import os

def clear_console():
    if os.name == 'nt': os.system('cls') 
    else: os.system('clear')

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        firstword = strs[0]
        for word in strs:
            while not word.startswith(firstword):
                firstword = firstword[:-1] # strings are immutable — this creates a new string
        return firstword

strs = []
while True:
    print('Enter quit to quit')
    word = str(input('Enter a word: '))
    if word == 'quit': break
    clear_console()
    strs.append(word)

print(strs)

if not strs:
    print('No words entered')
else:
    print(Solution().longestCommonPrefix(strs))

