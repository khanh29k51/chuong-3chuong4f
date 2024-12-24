s = input().strip() 
s = ' '.join(s.split()) 
s = s[0].upper() + s[1:] if s else ""
print(s) 