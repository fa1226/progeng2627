#exam grade problem
#subroutine to determine grade
def Result(Mark): 
      if Mark >= 80: 
          return 9,0 
      elif Mark >= 67: 
          return 8, 80 - Mark
      elif Mark >= 54:
          return 7, 67 - Mark 
      elif Mark >= 41: 
          return 6, 54 - Mark 
      elif Mark >= 31: 
          return 5, 41 - Mark 
      elif Mark >= 22: 
          return 4, 22 - Mark

#main program
print(Result(int(input("Number of marks:"))))





