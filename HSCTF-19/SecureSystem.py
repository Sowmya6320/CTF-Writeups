from pwn import *
import string

str_ = string.letters + string.digits + string.punctuation
m = "hsctf{h0w_d3d_y3u_de3cry"
indx = 50

conn = remote("crypto.hsctf.com" , "8111")
conn.recvuntil("super secret message: ")
ct = conn.recvline().strip()
conn.recvuntil("\n")
while(True):
	for i in str_:
		conn.recvuntil("you want to encrypt: ")
		conn.sendline(m + i)
		conn.recvuntil("\n")
		conn.recvuntil("Encrypted: ")
		tmp = conn.recvline().strip()
		conn.recvuntil("\n")
		if tmp == ct[:indx]:
			m = m + i
			break
	indx = indx + 2 
	if indx > 106:
		break
print m
		

#flag: hsctf{h0w_d3d_y3u_de3cryP4_th3_s1p3R_s3cuR3_m355a9e?}
