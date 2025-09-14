How to program things for mooncake


edit the list "input_list" to strings containing your operations, one on each line.

##for current version, this is line 251
  

you can assign variables to numbers on line 30 of the program

##note: variable numbers are automatically created based on how far along the list the number is
  
##note 2: the 64th variable is 16 bits of input (not sure what order rn)
  

    all integers are unsigned, and numbers are zero based


here's how player movement would look


    def(in_read):
      63=r31*65521 
        #sets input to itself with only the first four bits remaining.
        #variable 63 is input
      f0=31*65534
      f1=31*65533   
      f2=31*65531 
      f3=31*65522  
        #probably bad bitmasks to single out individual bits  
      if f0==1:     
        x=x+1     
      if f1==1:       
        x=x-1 
      if f2==1:       
        y=y+1
      if f3==1:
        y=y-1
        #movement directions added to x and y
