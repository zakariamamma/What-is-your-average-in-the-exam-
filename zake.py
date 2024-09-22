# hello guy's now un this project we created a topic for AI
"""
if you want to read simple code you can use this code 
x = "hello world"
print(x)
"""
x, y, z = "Nice job is perfect", "ok is not bad but not very good","no is very bad go to your room "

while True:
  value = input("\033[32m What is your average in the exam? => \033[0m")
  if int(value) >= 60 and int(value) <= 100:
    print(x)
    break
  elif int(value) >= 100:
    print(" yo lie")
    continue
  elif int(value) >= 50 and int(value) <= 60:  
    print(y)
    break
  elif int(value) <= 49:
    print(z)
    break

  else:
    print("i say What is your average in the exam? => ")
    continue
  
    
