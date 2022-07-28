# -*- coding: utf-8 -*-
"""recursiveStuff.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n39MZxaX0AR48fYFSZnWs8XutBe-oEcH
"""

import copy

#POWER SET CODE
lst = [1, 2, 3]

def insert_elem_into_each_list(lst, n):
  for i in lst:
    i.append(n)
    i.sort()
  return lst

def power_set(lst):
  #base case is empty list
  if len(lst) == 1:
    return [[]] + [lst]  
    
  smaller_ans = power_set(lst[1:])

  small_ansCopy = copy.deepcopy(smaller_ans) #copy the list because the funcion changes smaller list when you pass it in 
  
  remaining_ans = insert_elem_into_each_list(smaller_ans, lst[0])

  return small_ansCopy + remaining_ans


ret = power_set(lst)
ret.sort()
print(ret)

#EVAL CODE

def eval(s):
  if s[0] != '+' and s[0] != '-':
    s = '+' + s
  location_of_plus = [x for x in range(0, len(s)) if s[x] == "+"]
  location_of_minus = [x for x in range(0, len(s)) if s[x] == "-"]

  comb_locations = location_of_plus + location_of_minus 
  comb_locations.sort()

  if len(comb_locations) == 1:
    return int(s)
  location = comb_locations[-1]

  if s[location] == '-':
    return eval(s[:location]) + int(s[location:])
  else:
    return eval(s[:location]) + int(s[location+1:])

eval("4+4+4+4-10-23")

