def make_caps_initials(name):
	#create capitalized initials
	initials = ""
	splitname = name.split()
	for x in splitname:
		initials += x[0]
	initials = initials.upper()
	return(initials)

print(make_caps_initials(input("Please enter your name:")))
