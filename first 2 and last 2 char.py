def string_both_ends(str):  
  if len(str) < 2:  
    return ''  
  
  return str[0:2] + str[-2:]  
  
print(string_both_ends('t7Tech'))  
print(string_both_ends('t7'))  
print(string_both_ends('t'))  
 
