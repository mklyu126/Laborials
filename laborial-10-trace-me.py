


# def main():
#     a = False
#     b = True
#     c = True

#     if a or not b and c:
#         print("expression is true")
#     else:
#         print("expression is false")

# # main()

# #b and c = False 
# #a or not (false)
# #false or true
# # its going to print expression is false 

# # Part 2: Code Synthesis 

amount = float(input('What is the dollar amount of the current order?'))
min_free_del_amt = 40


def main():
    if amount < 0:
        
        print ('Invalid entry, orders must be positive')
    elif amount >= 0 and amount < min_free_del_amt:
        print ('Add $', f'{(min_free_del_amt - amount):.2f}', 'to your order to get free delivery')
    else:
        free_delivery()

def free_delivery():
    if amount >= min_free_del_amt:
        print ('You get free delivery!')
  
  
main()
