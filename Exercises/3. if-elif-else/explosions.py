#############################################################
#  Συγγραφέας   Δημήτρης Κάντζας
#  email        dimitriosk07 [at] gmail [dot] com
#  Ενότητα      3.if
#  Κατηγορία    Ηλιακό σύστημα
#############################################################

'''
Ο συγκεκριμένος κώδικας ελέγχει αν πέντε γνωστά αστέρια θα καταλήξουν
σε πλανητικό νεφέλωμα ή υπερκαινοφανή βάσει της μάζας τους.
'''

#############################################################
# Ας δούμε το μέλλον μερικών κοντινών αστεριών
#############################################################

#Η λίστα με τα αστέρια που θα μελετήσουμε:
stars = ['Ήλιος','Εγγύτατος Κενταύρου','Μπετελγκέζ','Αντάρης','Βέγας','Ρίγκελ']

#Οι μάζες των παραπάνω αστεριών είναι:
mass = [1,0.12,18,12.5,2.1,21] #σε ηλιακές μάζες

#############################################################
# Ας δούμε ένα-ένα τα αστέρια σε τι θα καταλήξουν!
#############################################################

# Ήλιος:
if mass[0]<8:
    print('O',stars[0],'θα καταλήξει σε πλανητικό νεφέλωμα!\n')
else:
    print('O',stars[0],'θα καταλήξει σε υπερκαινοφανή!\n')

# Εγγύτατος Κενταύρου:
if mass[1]<8:
    print('O',stars[1],'θα καταλήξει σε πλανητικό νεφέλωμα!\n')
else:
    print('O',stars[1],'θα καταλήξει σε υπερκαινοφανή!\n')

# Μπετελγκέζ:
if mass[2]<8:
    print('O',stars[2],'θα καταλήξει σε πλανητικό νεφέλωμα!\n')
else:
    print('O',stars[2],'θα καταλήξει σε υπερκαινοφανή!\n')

# Αντάρης:
if mass[3]<8:
    print('O',stars[3],'θα καταλήξει σε πλανητικό νεφέλωμα!\n')
else:
    print('O',stars[3],'θα καταλήξει σε υπερκαινοφανή!\n')

# Βέγας:
if mass[4]<8:
    print('O',stars[4],'θα καταλήξει σε πλανητικό νεφέλωμα!\n')
else:
    print('O',stars[4],'θα καταλήξει σε υπερκαινοφανή!\n')

# Ρίγκελ:
if mass[5]<8:
    print('O',stars[5],'θα καταλήξει σε πλανητικό νεφέλωμα!\n')
else:
    print('O',stars[5],'θα καταλήξει σε υπερκαινοφανή!\n')

