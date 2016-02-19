# This function takes the input of your current monthly income and the optional years to retirement
# parameter and outputs the equivalent needed to maintain current life style with an average of
# 2.5% inflation over time


from sys import argv

# income_needed_to_maintain_current_lifestyle_at_retirement

def income_needed(current_monthly_inc, years=30):
	x = current_monthly_inc
	for i in range(years):
		y = x * .025
		x = x + y
	return x


def run_func():
	x = 0
	y = 0
	try:
		x = int(argv[1])
		y = int(argv[2])
	except:
		try:
			x = int(argv[1])
		except:
			raise ValueError("Please enter your current monthly income")
	if x > 0 and y > 0:
		return income_needed(x, years=y)
	elif x > 0 and y <= 0:
		return income_needed(x)
	else:
		print("an error occured")

print(run_func())
