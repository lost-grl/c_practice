weight = 41.5
#Ground shipping
if weight == 0:
  print("error")
if weight <= 2:
  cost = (1.50 * weight) + 20
elif (weight > 2) and (weight <= 6):
  cost = (3.00 * weight) + 20
elif (weight > 6) and (weight <= 10):
  cost = (4.00 * weight) + 20
else:
  cost = (4.75 * weight) + 20
print("Ground Shipping Cost: ", cost)
premium_cost = cost + 125.00
print("Premium Ground Shipping Cost: ", premium_cost)

#Drone shipping
if weight == 0:
  print("error")
if weight <= 2:
  dcost = (weight * 4.50)
elif (weight > 2) and (weight <= 6):
  dcost = (weight * 9.00)
elif (weight > 6) and (weight <=10): 
  dcost = (weight * 12.00)
else: 
  dcost = (weight * 14.25)
print("Drone Shipping Cost: ", dcost)

#test
if weight == 4.8:
  print("For a 4.8 lb package, ground shipping is cheapest: ", cost)
if weight == 41.5:
  print("For a 41.5 lb package, gound shipping is cheapest: ", cost)