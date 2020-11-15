def pos(word, txt):
  first = word[0]
  for x in range(len(txt)):
    if first == txt[x]:
      sub = txt[x:x+len(word)*2:2]
      if word == sub:
        return x
  
  return -1

print(pos("a", "") == -1)
print(pos("hsal", "Mary has a little lamb")==5)

