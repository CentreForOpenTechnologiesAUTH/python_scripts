aDict = dict(zip('abcdefghijklmnopqrstuvwxyz.!?()-ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                              ['00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001',
                              '11010','11011','11100','11101','11110','11111',
                              '00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001'])) #the function from our alphabet to 5-bit binary strings
							  
def list_to_string(l):
    return ''.join(str(e) for e in l)

# btext is a binary string of the form 'something...'
# key is a binary string of the form '01010...'
# the result of the function is xoring bit-bit the btext with the key

def string_xor(btext,key): 
    cipher = []
    if len(btext)!=len(key):
        print("key and message must have the same lengths!")
        return 0
    for i in range(len(btext)):
        cipher.append(int(btext[i])^int(key[i])) #xoring bit-bit
    cipher = ''.join(str(e) for e in cipher)
    return cipher

# the function below converts a text of the form 'something' to 
# a binary string according to our 5-bit encoding


def text_enc(text):
    text = text[::-1]
    length = len(text)
    coded_text = ''
    for i in range(length):
        coded_text = aDict[text[i]]+ coded_text
    return coded_text.lower()
	
	
# The function below converts a binary string to an alphabetic text 
# according to our 5-bit encoding

def text_dec(binary_string):
    length = len(binary_string)
    inv_map = {v: k for k, v in aDict.items()}
    decoded_text = ''
    for i in range(0,length,5):
        decoded_text = inv_map[binary_string[i:i+5]] + decoded_text # + in strings is the join function.
    decoded_text = decoded_text[::-1]
    return decoded_text.lower()
	

# the function sumxor
# accepts a binary list of the form [1,0,1,...]
# and returns the xor-sum of the bits

from collections import deque
def sumxor(l):
    r = 0
    for v in l: 
        r = r^v
    return r

# the function lfsr accept three arguments
# seed : a binary list of the form [0,1,1,1,0,1,0,1,...] which is the initial seed
# feedback : a binary list which defined the feedback polynomail 
# for instance [0,0,1,1]-->x^4+x^3+1
# bits : is an integer, which telles the function to return bits-number if the stream of lfsr
# the function prints the internal states if flag = 0 and always returns the output

def lfsr(seed,feedback,bits, flag):
    index_of_ones = []
    feedback_new = []
    for i in range(len(feedback)):
        if 1 in feedback:
            index_of_ones.append(feedback.index(1))
            feedback[feedback.index(1)] = 0
    feedback_new = index_of_ones    #this is a list which contains the positions of 1s in feedback list
    seed = deque(seed)              # make a new deque 
    output = []
    if flag==0:
        print('initial seed :',seed)
    for i in range(bits):
        xor = sumxor([seed[i] for i in feedback_new])
        output.append(seed.pop()) #extract to output the right-most bit of current seed
        seed.appendleft(xor)      #insert from left the result of the previous xor 
        if flag==0:
            print('state', i+1, 'of the lfsr :',seed)
    return output