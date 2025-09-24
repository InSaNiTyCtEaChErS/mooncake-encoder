How to program things for mooncake

ifs can only go up to 4 layers deep because of else cases (12 spaces, in increments of 4)

edit the file named "input_program" with your program that you want to compile
  
you can assign variables to numbers on line 18 of the program (just add a variable and it'll be assigned, for up to 128 variables total)

###note: variable numbers are automatically created based on how far along the list the number is
  
###note 2: the 64th variable is 16 bits of input (not sure what order rn)

    hotbar control variables are 61, 62, and 63. 61 selects a slot to set to (0 based) and 62-63 directly control a 3 bit per pixel 3*3 display next to each item
  

    all integers are unsigned, and numbers are zero based


here's how player movement would look


     0  def(move):
     1    63=r31*65521 
     2      #sets input to itself with only the first four bits remaining.
     3      #variable 63 is input
     4    f0=31*65534
     5    f1=31*65533   
     6    f2=31*65531 
     7    f3=31*65522  
     8      #probably bad bitmasks to single out individual bits  
     9    if f0==1:     
    10      x=x+1     
    11    if f1==1:       
    12      x=x-1 
    13    if f2==1:       
    14      y=y+1
    15    if f3==1:
    16      y=y-1
    17      #movement directions added to x and y

here's fibbonachi as another example

    0  def(fibbonachi):
    1    f0=1
    2    f1=f0+f1
    3    f0=f1+f0
    4    branch2

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


        
