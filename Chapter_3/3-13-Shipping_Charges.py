# 3-13 Shipping Charges

# The Fast Freight Shipping Company charges the following rates:
# Weight of Package                          Rate per Pound
# 2 pounds or less                              $1.50
# Over 2 pounds but not more than 6 pounds      $3.00
# Over 6 pounds but not more than 10 pounds     $4.00
# Over 10 pounds                                $4.75
# Write a program that asks the user to enter the weight of a package
# and then displays the shipping charges.

# Set the shipping charges.
shipping_charge = 0

# Get the weight of the package.
package = float(input('Enter the weight of the package: '))

# Determine the shipping charges.
if package <= 2:
    shipping_charge = package * 1.50
else:
    if package > 2 and package <= 6:
        shipping_charge = package * 3.00
    else:
        if package > 6 and package <= 10:
            shipping_charge = package * 4.00
        else:
            shipping_charge = package * 4.75

# Display the results.
print('Shipping Charge: $', format(shipping_charge, ',.2f'), sep='')

