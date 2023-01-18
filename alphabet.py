import sys

s = sys.stdin.readline()
atoz = list("abcdefghijklmnopqrstuvwxyz")

[print(s.find(alphabet),end ='') for alphabet in atoz]