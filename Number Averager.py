thevals = input("What numbers to average (separate by commas)>>> ")
val = thevals.split(",")
mytup = tuple(val)
div, summ = 0, 0
for i in mytup:
    div += 1 
    summ += float(i)
########################
print("\nThe average between the %s values is %.1f" %
      (div, summ/div))
print("-----------------------------------" + "-" * len("%.1f" % (summ/div)), end = "")
print("-" * len("%s" % (div)))