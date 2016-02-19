import sys

try:
    cost = int(sys.argv[1])
    term = int(sys.argv[2])
    rate = float(sys.argv[3])

    def overpay_for_car(cost, term, rate):
        original = cost
        for x in range(term):
            a = cost * rate
            cost = cost + a
        return cost - original

    print("You will pay {} over the original amount of {} for the car with a {} year term and {} interest rate".format(overpay_for_car(cost, term, rate), cost, term, rate))
    print('....................................................')
except:
    print("Please provide system argments. \n.....................\nFormat: caroverpayment.py cost term interest_rate\n.....................")
