weight = 41.5

#Ground shipping
gscost = 20 #Flat charge, missing weight cost
if weight > 10:
  gscost += 4.75 * weight
elif  weight > 6:
  gscost += 4.00 * weight
elif  weight > 2:
  gscost += 3.00 * weight
else:
  gscost += 1.50 * weight

#Ground shipping premium
gspcost = 125.00 #Only has Flat charge

#Drone Shipping
dscost = 0.00 #No Flat charge, missing weight cost
if weight > 10:
  dscost += 14.25 * weight
elif  weight > 6:
  dscost += 12.00 * weight
elif  weight > 2:
  dscost += 9.00 * weight
else:
  dscost += 4.50 * weight

print("Ground shipping: " + str(gscost))
print("Ground shipping premium: " + str(gspcost))
print("Drone Shipping: " + str(dscost))