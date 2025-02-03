#!/usr/bin/env python
# coding: utf-8

# In[ ]:


notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
soflege_scale = [['Do','Re','Mi','Fa','So','La','Ti'],[0,2,4,5,7,9,11]]
def note(MS,soflege_note):
  for i,x in enumerate(soflege_scale):
    if soflege_note in x:
      co = (i,x.index(soflege_note))
      co = list(co)
      co[0]+=1
      break
  number = soflege_scale[co[0]][co[1]]
  MS_no=notes.index(MS)
  final_i = MS_no + number
  if final_i > 11:
    final_i -=12
  return(notes[final_i])
MS = input("Please Enter Major Scale: ")
soflege_note=input("Please Enter Soflege Note: ")
print(note(MS,soflege_note))

