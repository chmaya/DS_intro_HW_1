# chmaya gabriel adda 315701847
# A

def my_func (x1, x2, x3):
    sum_of_all = x1 + x2 + x3
    if (sum_of_all == 0):
       return print("Not a number – denominator equals zero")
    if ((type(x1) or type(x2) or type(x3)) == int):
        return print("Error: parameters should be float")
    value_of_fun = (sum_of_all *(x2 + x3) * x3) / sum_of_all 
  
    return float(sum_of_all)

# B

def convert(hours, minutes):

    if (hours < 0 or minutes < 0 ):
        return print("Input error!")
    hours_in_second = hours * 3600
    minuts_in_second = minutes * 60
    sum_of_all = hours_in_second + minuts_in_second

    return print(sum_of_all)

