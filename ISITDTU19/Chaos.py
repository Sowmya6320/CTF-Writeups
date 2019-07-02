from pwn import *
import string

punctuation = "~`!@#$%^&*()_-+=<,>.?|"
def chaos_tool(strr):
	key = ""
	for i in strr:
		if (len(i) == 11):
			if(i[6] in punctuation):
				key = key + i[3]
			else: 
				key = key + i[6]
		elif (len(i) == 8):
			key = key + i[0]
		elif (len(i) == 14):
			key = key + i[-1]	
	return key

io = remote('104.154.120.223' ,'8085')
inp = io.recvuntil("Your choice: ")
k = list(inp.split(" "))
ll = k[7:71]
ll[-1] = ll[-1][:-8]
key = chaos_tool(ll)
io.sendline('2')
io.recvuntil("Please enter the key to get flag: ")
io.sendline(key)
print io.recv()
