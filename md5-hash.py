import md5
#counter = 0

pwfile="passwords"
try:
	pwfile = open(pwfile, "r")
except:
	print "File not found \n"
	quit()
c = 0
for password in pwfile:
	c = c+1
	filemd5 = md5.new(password.strip()).hexdigest()
	print "User"+str(c)+":"+str(filemd5)


