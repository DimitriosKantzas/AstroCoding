#############################################################
#  Συγγραφέας   Δημήτρης Κάντζας
#  email        dimitriosk07 [at] gmail [dot] com
#  Ενότητα      4.for
#  Κατηγορία    νόμος Hubble–Lemaître
#############################################################


'''
Στον κώδικα αυτό αξιοποιούμε το νόμο Hubble–Lemaître για να
υπολογίσουμε την ταχήτυτα απομάκρυνσης κάποιων γνωστών
γαλαξιών (Άσκηση 9 από τις διαφάνειες).
'''


#############################################################
# Ορίζουμε αρχικά τη σταθερά του Hubble που συνδέει την απόσταση  d
# ενός γαλαξία με την ταχήτυτά του  u  μέσω της εξίσωσης:
# u = H0*d
#############################################################

H0 = 20 #km/s/Mly


#############################################################
# Ορίζουμε δυο λίστες, η μία με τα ονόματα των γαλαξιών, και η
# δεύτερη με τις αποστάσεις τους από το δικό μας.
#############################################################

distances = [10, 23, 35, 42, 72] #Mly -- floats
names = [55, 4945, 5055, 3521, 4487] #NGC -- int/str


#############################################################
# Ορίζουμε μια κενή/άδεια λίστα στην οποία θα προσθέτουμε τις
# ταχύτητες των γαλαξιών όπως υπολογίζονται από το νόμο του Hubble
#############################################################
velocities = []


#############################################################
# Υπολογίζουμε την ταχύτητα για κάθε έναν από τους παραπάνω
# γαλαξίες βάσει της απόστασής τους.
#############################################################

for i in range(0,len(distances)): 
    #όπου len(distances) δίνει το μέγεθος της λίστας distances

    '''
    Ορίζουμε μια μεταβλητή που έχει αριθμητική τιμή ίση με την
    απόσταση καθενός από τους γαλαξίες
    '''
    d=distances[i] #σε Mly -- εκατομμύρια έτη φωτός

    '''
    Υπολογίζουμε την ταχήτυτα απομάκρυνσης του εκάστοτε γαλαξία
    από το νόμο του Hubble:
    '''
    velocity = H0*d

    '''
    Τυπώνουμε το αποτέλεσμά μας:
    '''
    print('H ταχύτητα του γαλαξία NGC',names[i],'είναι',velocity,'km/s.\n')

    '''
    Με την παρακάτω εντολή, αποθηκεύουμε την ταχύτητα του
    εκάστοτε γαλαξία στην αντίστοιχη λίστα που έχουμε
    ορίσει έξω από τη for loop.
    '''
    velocities.append(velocity)

    
###########################################################################
# Ερώτημα 1: Ένας γαλαξίας που απομακρύνεται με 850 km/s από το Γαλαξίας μας,
# σε τι απόσταση βρίσκεται;
###########################################################################

#Λύνουμε το νόμο των Hubble–Lemaître ως προς την απόσταση, επομένως
# d = u/H0

u = 850 #km/s η ταχύτητα απομάκρυνσης του γαλαξία

#Από το νόμο των Hubble–Lemaître:
d = u/H0
print('\nO γαλαξίας αυτός που ταξιδεύει με',u,
      'km/s βρίσκεται σε απόσταση',d,'Mly')

###########################################################################
# Ερώτημα 2: Ο γαλαξίας της Ανδρομέδας ταξιδεύει με ταχύτητα -300 km/s.
# Σε τι απόσταση βρίσκεται σύμφωνα με το νόμο των Hubble–Lemaître;
###########################################################################

u = 300 #km/s η ταχήτυτα απομάκρυνσης του γαλαξία της Ανδρομέδας

d = u/H0
print('\nO γαλαξίας της Ανδρομέδας απέχει',d,'Mly από το Γαλαξίας μας.')





