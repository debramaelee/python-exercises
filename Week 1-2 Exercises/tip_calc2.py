bill_amount = float(raw_input("Total bill amount? "))
service_lvl = raw_input("Level of service? ")
split_num = int(raw_input("Split in how many ways? "))

if service_lvl == "bad":
    tip_percent = 0.10 * bill_amount
elif service_lvl == "fair":
    tip_percent = 0.150 * bill_amount
elif service_lvl == "good":
    tip_percent = 0.20 * bill_amount

print "Tip amount: $%.2f" % tip_percent
total_amount = bill_amount + tip_percent
print "Total amount: $%.2f" % total_amount

amount_after_split = total_amount / split_num
print "Amount per person: $%.2f" % amount_after_split
