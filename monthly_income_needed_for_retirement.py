# This function takes the input of your current monthly income and the optional years to retirement
# parameter and outputs the equivalent needed to maintain current life style with an average of
# 2.5% inflation over time


from sys import argv

# income_needed_to_maintain_current_lifestyle_at_retirement

def income_needed(current_monthly_inc, years=30, inflation_rate=0.025):
	x = current_monthly_inc
	for i in range(years):
		y = x * inflation_rate
		x = x + y
	return x

def find_kwargs():
	"""
		Returns a dictionary of keyward arguments with their values
	"""
	empt_dict = {}
	for i in range(len(argv)):
		if argv[i].split("="):
			t = argv[i].split("=")
			try:
				empt_dict[t[0]] = t[1]
			except IndexError:
				continue
		else:
			pass
	return empt_dict



def run_func():
	x = 0
	y = 0
	z = 0
	kwargs = find_kwargs()
	for key in kwargs:
		if key == "inflation_rate":
			z = float(kwargs[key])
		elif key == 'years':
			y = int(kwargs[key])
	try:
		if x == 0 and y == 0:
			x = int(argv[1])
			if z == 0:
				y = int(argv[2])
	except:
		try:
			x = int(argv[1])
		except:
			print("Please try again with your monthly income")
	if x > 0 and y > 0 and z > 0:
		return income_needed(x, years=y, inflation_rate=z)
	elif x > 0 and y > 0 and z <= 0:
		return income_needed(x, years=y)
	elif x > 0 and y <= 0 and z <= 0:
		return income_needed(x)
	elif x > 0 and y <=0 and z > 0:
		return income_needed(x, inflation_rate=z)
	else:
		raise Exception("An error has occured")

print(run_func())
