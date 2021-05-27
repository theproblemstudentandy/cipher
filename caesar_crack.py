# can input negative

import pyinputplus as pyin  
cipher_text = pyin.inputStr(prompt="Please input your cipher text:")
shift_flag = pyin.inputYesNo(prompt="Do you know the shift?(yes/no)") #to do: check shift must bigger than 0

def caesar(shift):
	plain_text=""
	for letter in cipher_text:
		n = ord(letter)
		if n<=90 and n>=64: #check is alphabet or not
			n+=shift
			if n>90:
				n = n-90+64
			elif n<64:
				n = 91+(n-64)

		elif n>=97 and n<=122:
			n+=shift
			if n>122:
				n = n-122 + 96
			elif n<97:
				n = 123 + (n-97)
			
		plain_text+=chr(n)
	print(shift,":",plain_text)	

if shift_flag=="yes":
	shift = pyin.inputInt(prompt="Please input your shift:")
	caesar(shift)
else:
	for i in range(-13,14):
		caesar(i)

