#############################################################
#  Συγγραφέας   Δημήτρης Κάντζας
#  email        dimitriosk07 [at] gmail [dot] com
#  Ενότητα      3.if
#  Κατηγορία    Αστέρια
#############################################################


'''
Με τον παρών κώδικα θα εξετάσουμε σε ποιο μήκος κύματος εκπέμπουν
τρια αντικείμενα της Φύσης: ο άνθρωπος, ο Ήλιος και ο Σείριος Α.
'''


#############################################################
#Ερώτημα 2:
#############################################################


#Ορίζουμε τις θερμοκρασίες σε βαθμούς Kelvin
T_human = 305 #θερμοκρασία του ανθώπου (human) σε Κ
T_sun = 5778  #θερμοκρασία του ήλιου (sun) σε K
T_sir = 9940  #θερμοκαρίσα του Σείριου (Sirius) σε K



#############################################################
# Ερώτημα 3:
#############################################################

'''
To μήκος κύματος (λ) της εκπεμπόμενης ακτινοβολίας εξαρτάται
από τη θερμοκρασία (Τ) του σώματος που ακτινοβολεί, και δίνεται
από το νόμο του Wien: λ=2.898*10**6/Τ 
'''

#Ο άνθρωπος εκπέμπει σε μήκος κύματος:
L_human = 2.898*10**6/T_human #σε nm (1nm=10**(-9)m)

print('\nO άνθρωπος που έχει θερμοκρασία',T_human,'K εκπέμπει σε μήκος'\
      'κύματος',L_human,'nm.\n')


#Ο Ήλιος εκπέμπει σε μήκος κύματος: ΣΥΜΠΛΗΡΩΣΤΕ ΤΗΝ ΑΠΑΝΤΗΣΗ ΣΑΣ ΕΔΩ
#...

#Ο Σείριος Α εκπέμπει σε μήκος κύματος: ΣΥΜΠΛΗΡΩΣΤΕ ΤΗΝ ΑΠΑΝΤΗΣΗ ΣΑΣ ΕΔΩ
#...



#############################################################
# Ερώτημα 4:
#############################################################


#Ελέγχουμε αν ο άνθρωπος εκπέμπει στο UV, στο οπτικό ή στο IR: 
if 10<=L_human<400:
    print('\nΟ άνθρωπος εκπέμπει στο UV!\n')
elif 400<=L_human<700:
    print('\nΟ άνθρωπος εκπέμπει στο οπτικό!\n')
elif 700<=L_human<10**6:
    print('\nΟ άνθρωπος εκπέμπει στο IR!\n')
else:
    print('\nΟ άνθρωπος δεν εκπέμπει σε κανένα από τα παραπάνω!\n')

    
#############################################################
# Ερώτημα 5:
#############################################################


#Ελέγχουμε αν ο Ήλιος και ο Σείριος εκπέμπει στο UV, στο οπτικό ή στο IR:
#ΣΥΜΠΛΗΡΩΣΤΕ ΤΗΝ ΑΠΑΝΤΗΣΗ ΣΑΣ ΕΔΩ ...

