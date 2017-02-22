bill_amount = float(raw_input("Total bill amount? "))
service_lvl = raw_input("Level of service? ")

# ----------FIRST ATTEMPT did not show extra 0 after dec.
# if service_lvl == "bad":
#     tip_percent = '{:,.2f}'.format(.15 * bill_amount)
# elif service_lvl == "fair":
#     tip_percent = '{:,.2f}'.format(.18 * bill_amount)
# elif service_lvl == "good":
#     tip_percent = '{:,.2f}'.format(.2 * bill_amount)
#
# print "Tip amount: $%s" % tip_percent
# bill_amount = '{:,.2f}'.format(bill_amount)
# print "String bill_amount: %s" % bill_amount
# bill_amount = float(bill_amount)
# print bill_amount
# total_amount = str(float(bill_amount) + float(tip_percent))
# print total_amount

# print "Total amount: $%s" % total_amount

if service_lvl == "bad":
    tip_percent = .10 * bill_amount
elif service_lvl == "fair":
    tip_percent = .15 * bill_amount
elif service_lvl == "good":
    tip_percent = .2 * bill_amount

total_amount = bill_amount + tip_percent
print "Tip amount: $%.2f" % tip_percent
print "Total amount: $%.2f" % total_amount
