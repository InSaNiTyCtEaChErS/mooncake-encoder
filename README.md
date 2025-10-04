How to program things for mooncake

ifs can only go up to 4 layers deep because of else cases (12 spaces, in increments of 4)

edit the file named "input_program" with your program that you want to compile
  
you can assign variables to numbers on line 18 of the program (just add a variable and it'll be assigned, for up to 128 variables total)

###note: variable numbers are automatically created based on how far along the list the number is
  
###note 2: the 64th variable is 16 bits of input (not sure what order rn)

    hotbar control variables are 61, 62, and 63. 61 selects a slot to set to (0 based) and 62-63 directly control a 3 bit per pixel 3*3 display next to each item
  

    all integers are unsigned, and numbers are zero based


here's how player movement would look


       def(move):
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

here's fibbonachi as another example

       def(fibbonachi):
         f0=1
         f1=f0+f1
         f0=f1+f0
         branch2

and last but not least, cosine.

        Def cosine
        f0=fin*fin
        f0=405*f0
        f0=0-f0+1
        f1=0-fin
        f1=f1*f1
        f1=0-405*f1-1
        f2=f0*f1
        If f2 >= 0
            f5=f2/8
        Else
            f5=0-f2/8
        f5=f5*8/9
        fout=f5


        
