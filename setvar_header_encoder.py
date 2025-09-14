#meow

print('hello')

#time to define tables

table = {
    '+' :0b00000,
    '-' :0b00001,
    '*' :0b10000,
    '/' :0b10001
    }
table2 = {
    '<':0,
    '>':1,
    '=':2,
    '!':3
}
shapes ={
	0 :'C',
	1 :'R'
    }
colors ={
	0 :'u',1 :'r',2 :'y',3 :'g',4 :'c',5 :'b',	6 :'m',7 :'w'
    }
hex_convert={ #hex conversion table because the bytes.fromhex function wan't working
    'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}


vars_ = [ #variables!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    "fin","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","fout", #function variables
    "hp","x","y","z","ax","ay","az","level", #8 basic game variables

    #add more here if you want more!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    ]
ascii_ = "abcdefghijklmnopqrstuvwxyz012345"
def ascii_enc(in_):
    out = ""
    for char in in_:
        out += ascii_.find(char)
        out *= 32
    out /= 32
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
    for char in input_:
        if char == " ":
            header += 1
    header = header // 4
    input_ += " "
    input_ = input_.lstrip(" ")
    if ("="in input_) and not ("if" in input_):
        try:
            varset = int(input_[0:(int(input_.find("=")))])
        except:
            varset = vars_[(input_[0:(int(input_.find("=")))])]  #try understanding this line
        for char in input_[int(input_.find("="))+1:-1]:
            if char == "#":
                break
            if char in "+-*/":
                operations += table[char]*(2^i)
                i+=1
                if var >= 1:
                    if var >= 2 and var != "r":
                        variables.append[vars_[varname]]
                    else:
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
            if "r" in num:
                vars_ *= 256
                vars_ += int("0"+num[1:-1])
            else:
                nums_ *= 65536
                nums_ += int(num)
        #shifting them to align them for returning
        varset += header * 256
        varset *= 2^96
        vars_ *= 2^64
        nums_ += vars_ + varset
        return(nums_*8)
    elif "if" in input_:
        input_=input_[3:-1] #removing the "if "
        for char in input_:
            if char == ":" or char == "#":
                break
            if char == "r":
                var = 1
            if char in "abcdefghijklmnopqrstuvwxyz":
                var += 2
                varname += char
            elif char in "0123456789" and var != 1:
                varname += char
            if char in "0123456789":
                var *= 10
                var += int(char)
            elif char in "<>=!":
                vars_ *= 256
                if var == 1:
                    vars_ += var
                    var = 0
                else:
                    vars_ += vars_[varname]
                operations += table2[char]
                operations *= 8
            elif char in "aox|": #| is a sign to or instead of and all the operands together!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                if char == "a":
                    num += 1
                elif char == "o":
                    num += 2
                else:
                    num += 4
                num *= 8
            else:
                print("invalid char in if: "+char)
        return((((vars_+operations*(2^32))*(2^18)+num*8)+header)*8+1)
    elif "branch" in input_:
        return(2+(int(input_[6:-1])*16+header)*8)
    elif "save" in input_:
        return(3+(int(input_[4:-1])*16+header)*8)
    elif "load" in input_:
        return(4+(int(input_[4:-1])*16+header)*8)
    elif "gpu" in input_: #gpu 0-1
        input_ = input_[3:-1]
        num = int(input_[0:input_.find("-")])
        var = int(input_[input_.find('-')+1:-1])#
        output = num*65536 + var #number to set from, then number to set to. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return(5+(output*16+header)*8)
    elif "def" in input_:
        input_ = input_[3:-1]
        output = ascii_enc(input_)
        return (6+(output*16+header)*8)
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

MAX_X = 37

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
            ent["Y"] = num // MAX_X * 8
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

instruction_order = [6,4,0,0,1,0,0,1,0,0,1,0,0,1,5,5,5,5,2,
                     4,0,0,1,0,0,1,0,0,1,0,0,1,5,5,5,5,2,3
                     ]
print(len(instruction_order))
input_list = [ 
    '#fibbonachi',
    '0=1',
    '1=r0',
    '2=r1+r0',
    'if63=3:',
    '    branch1'
    ]

output = ""
output_1 = ""
line = 0
instruction_index = 0
for item in input_list:
    if item[0] != "#":
        output_1 += str(encodev2(item))
        while True:
            if int(output_1)%8 != instruction_order[instruction_index]:
                output += "\
                "
                instruction_index += 1
                instruction_index %= len(instruction_order)
            else:
                break
        instruction_index += 1
        instruction_index %= len(instruction_order)
        output += convert(output_1)
        output+="\
        "
        line += 1
    else:
        print("comment: "+ item)

outputs = makeConstants(output)

print('!!donw!!')
print(outputs)
