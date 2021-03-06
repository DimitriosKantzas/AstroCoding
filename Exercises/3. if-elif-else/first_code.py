#############################################################
#  Συγγραφέας   Δημήτρης Κάντζας
#  email        dimitriosk07 [at] gmail [dot] com
#  Ενότητα      3.if
#  Κατηγορία    Ηλιακό σύστημα
#############################################################


#Ορίζουμε πρώτα τις σταθερές του προβλήματος:
mass_Earth = 5.972*10**(24) #μάζα της Γης σε kg
AU = 149*10**6              #Astronomical Unit= μέση απόσταση Γης-Ήλιου σε km

#Ορίζουμε τις μεταβλητές του προβλήματος:
planet_name = 'Γη'	    # Tο όνομα του πλανήτη. 
planet_mass = 1*mass_Earth  # Η μάζα του παραπάνω πλανήτη. 
planet_distance = 1*AU	    # Η απόσταση του πλανήτη από τον Ήλιο.

#Τυπώστε παρακάτω τη μάζα και την απόσταση του πλανήτη. Μην ξεχάσετε τις μονάδες!
print(f'\nΟ πλανήτης {planet_name} βρίσκεται σε απόσταση {planet_distance} \
km από τον Ήλιο.')
