print("Welcome to the Real Estate Estimator")
property__square = float(
    input("Enter the size of the property in square feet: "))
property_location = input("Enter the location (city or suburb): ")

city_prize_per_sq = 250
subur_prize_per_sq = 150

if property_location.lower() == "city":
    estimated_price = property__square * city_prize_per_sq
    print("The estimated price for a", (property__square),
          "property in ", property_location, "is:", estimated_price)
elif property_location.lower() == "subur":
    estimated_price = property__square * subur_prize_per_sq
    print("The estimated price for a", property__square,
          "property in ", property_location, "is", estimated_price)

else:
    print("Try Again")
