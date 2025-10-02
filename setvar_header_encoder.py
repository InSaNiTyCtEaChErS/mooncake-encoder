#meow

print('hello')

#time to define tables

table = {'+' :0b00000,'-' :0b00001,'*' :0b10000,'/' :0b10001}
table2 = {'<':0,'>':1,'=':2,'!':3,'|':4}
shapes ={0 :'C',1 :'R'}
colors ={0 :'u',1 :'r',2 :'y',3 :'g',4 :'c',5 :'b',	6 :'m',7 :'w'}
hex_convert={ #hex conversion table because the bytes.fromhex function wan't working
    'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}


vars_l = [ #variables!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    "fin","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","fout", #function variables
    "hp","x","y","z","ax","ay","az","level", #8 basic game variables

    #add more here if you want more!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    ]

ascii_ = "abcdefghijklmnopqrstuvwxyz0123456789[](){}<>,._-"
def ascii_enc(in_):
    out = 0
    for char in in_:
        out += ascii_.find(char)
        out *= 48
    out /= 48
    return (out)

def encodev2(input_):
    print(str(line),": ",input_)
    varset=127
    i=0
    operations = 0b0
    var = 0
    vars_ =0
    num=0
    nums_ = 0
    header = 0
    variable = 0
    variables = []
    varname = ""
    input0 = input_
    input_ = ""
    header = header // 4
    for char in input0 :
        if char != " ":
            if char != "#":
                input_ += char
            else:
                break
    if ("="in input_) and not ("if" in input_):
        try:
            varset = int(input_[0:(int(input_.find("=")))])
        except:
            varset = vars_l.index(input_[0:(int(input_.find("=")))])   #try understanding this line
        for char in input_[int(input_.find("="))+1:-1]:
            if char in "+-*/":
                operations += table[char]*(2^i)
                i+=1
                if var >= 1:
                    try:
                        variables.append("r"+vars_l.index(varname))
                    except:
                        variables.append("r"+str(variable))
                else:
                    variables.append(num)
                var = 0
                num = 0
            elif char in "0123456789":
                if var == 1:
                    variable *=10
                    variable += int(char)
                elif var <= 0:
                    num *= 10
                    num += int(char)
            elif char == "r":
                var = 1
            elif char in "abcdefghijklmnopqrstuvwxyz0123456789":
                var += 2
                varname += char
            else:
                print("setvar instruction error here: "+input_)
        for num in variables:
            if "r" in str(num):
                vars_ *= 256
                vars_ += int("0"+num[1:-1])
            else:
                nums_ *= 65536
                nums_ += int(num)
        #shifting them to align them for returning
        varset = header * 8+ varset * 128
        varset *= 2^96
        vars_ *= 2^64
        nums_ += vars_ + varset
        return(nums_*8)
    elif "if" in input_:
        if "elif" in input_:
            input_=input_[5:-1]
        else:
            input_=input_[3:-1] #removing the "if "
        for char in input_:
            if char in "<>=!|":   # <> and != are used normally, but | tells the computer to or comparisons together
                operations += table2[char]
                operations *= 8
                try:
                    vars_ += vars_l.index(var)
                except:
                    vars_ += var
                var = 0
            elif char == "r":
                if variable == 0:
                    variable = 1
            elif char in "0123456789": #checking where to pu numbers
                if var == 0:
                    num += int(char)
                    num *= 10
                elif variable == 1:
                    var += int(char)
                    var *= 10
                else:
                    vars_+= char
            elif char in "abcdefghijklmnopqrstuvwxyz": #doing variable shenanigans
                variable += 2
                vars_+= char
            else:
                print("invalid char in if: "+char)
        return((((vars_+operations*(2^32))*(2^18)+num*8)+header)*8+1)
    elif "else" in input_:
        print(e)
        return(1+(header+4)*8)
    elif "branch" in input_:
        return(2+(int(input_[6:-1])*16+header)*8)
    elif "save" in input_: # save and load use an index from 0 to 524287 for where to save/load the upper 64 registers !!!!!!!!!!!!!!!!!!!!!!!!!!
        return(3+(int(input_[4:-1])*16+header)*8)
    elif "load" in input_:
        return(4+(int(input_[4:-1])*16+header)*8)
    elif "gpu" in input_: #gpu 0-1
        input_ = input_[3:-1]
        num = int(input_[0:input_.find("-")])
        vars_ = input_[input_.find('-'):-1]
        var = int(input_[input_.find('-')+1:-vars_.find('-')])#
        output = num*65536 + var #number to set from, then number to set to. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        nums_ = int(vars_[1:-1])
        return(5+(output*16+header+nums_*(2^20))*8)
    elif "def" in input_:
        input_ = input_[3:-1]
        output = ascii_enc(input_)
        return (6+(output*16+header)*8)
    elif "return" in input_:
        return (7+(header*8))
    elif "call" in input_:
        return(ascii_enc(input_[4:-1])*16+(header*8), "call")
    else:
        print("    invalid line: "+input_)

def convert(input_):
    output=''
    input_ = hex(int(input_))
    i=0
    input_ = input_[2::]
    for char in input_:
        if not (char in '0123456789'):
            char = hex_convert[char]
        char=int(char)
        output = output+shapes[int(0b01000 & char)/8]+colors[int(0b0111 & char)]
    i = 0
    output_shape = ''
    for char in output:
        i+=1
        if (i%8) == 1 and not i==1:
            output_shape = output_shape + ':'
        output_shape = output_shape + char
    #a shape buffer, probably not necessary as the input is padded in the previous function
    try:
        if output_shape[-9] != ':':
            output_shape = output_shape + 'Cu'
        if output_shape[-9] != ':':
            output_shape = output_shape + 'Cu'
        if output_shape[-9] != ':':
            output_shape = output_shape + 'Cu'
        if output_shape[-9] != ':':
            output_shape = output_shape + 'Cu'
    except IndexError:
        ":3"
    return output_shape
	
#borrowed signal generator code xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
import json
import gzip
import fileinput

from base64 import b64decode, b64encode

ENCODING = "utf-8"
BP_SIG = "SHAPEZ2-3-"

SIGNAL_TYPE = "ConstantSignalDefaultInternalVariant"

EMPTY_BP = """{
	"V": 1122,
	"BP": {
  	"$type": "Building",
  	"Icon": {"Data": ["icon:Buildings", null, null, "shape:CuCuCuCu"]},
  	"Entries": [],
  	"BinaryVersion": 1122
	}
}"""

def encodeValue(value):
	if (value.isdigit()):
		num = int(value)
		v = "\x03" + chr(num & 0xff) + chr((num >> 8) & 0xff) + "\x00\x00"
	else:
		# TODO: verify shape code
		v = "\x06\x01\x01" + chr(len(value)) + "\x00"  + value
	
	return b64encode(v.encode(ENCODING)).decode(ENCODING)

MAX_X = 38

def makeConstants(fileinput):
    bp = json.loads(EMPTY_BP)
    data = bp["BP"]["Entries"]
    num = 0
    line_ =""
    for line in fileinput:
        if line == "\
        ":
            value = line_.strip()
            ent = {}
            ent["X"] = num % MAX_X
            ent["Y"] = num // MAX_X * 4
            ent["R"] = 3
            ent["T"] = SIGNAL_TYPE
            ent["C"] = encodeValue(value)
            data.append(ent)
            num = num + 1
            line_ = ""
        else:
            line_ += line
    jdata = json.dumps(bp, separators=(",", ":")).encode(ENCODING)
    return BP_SIG + b64encode(gzip.compress(jdata)).decode(ENCODING) + "$" #end of borrowed code xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



# note: inputs are always set to variable 63!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

instruction_order = [6,4,0,0,1,0,0,1,0,0,1,0,0,1,5,5,5,5,
                     4,0,0,1,0,0,1,0,0,1,0,0,1,5,5,5,5,2,3,7
                     ]
print(len(instruction_order))
f=open("input_program.txt")
input_list = f.readlines()

output = ""
output_1 = ""
line = 0
instruction_index = 0
e=0

for item in input_list:
    if item[0] != "#":
        e=int(encodev2(item))
        try:
            output_1 += str(e[0])
            if e[1]=="call":
                while not instruction_index == len(instruction_order)-1:
                    instruction_index += 1
        except:
            output_1 += str(e)
            while True:
                if int(output_1)%8 != instruction_order[instruction_index]:
                    output += "null\
                    "
                    instruction_index += 1
                    instruction_index %= len(instruction_order)
                else:
                    break
        instruction_index += 1
        instruction_index %= len(instruction_order)
        output += convert(int(output_1)//8)
        output+="\
        "
        line += 1
    else:
        print("comment: "+ item)

outputs = makeConstants(output)

print('!!donw!!')
print(outputs)
