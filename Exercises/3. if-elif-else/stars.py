#############################################################
#  Συγγραφέας   Δημήτρης Κάντζας
#  email        dimitriosk07 [at] gmail [dot] com
#  Ενότητα      3.if
#  Κατηγορία    Αστέρια
#############################################################


'''
Ο παρών κώδικας χρησιμοποιεί ως δεδομένα δυο λίστες οι οποίες 
αντιστοιχούν: η πρώτη στα ονόματα γνωστών αστέρων του νυχτερινού ουρανού 
και η δεύτερη στις αποστάσεις τους από τη Γη. 
Με τον κώδικα αυτόν μπορούμε να βρούμε τον πλησιέστερο καθώς και τον
πιο απομακρυσμένο αστέρα από τις παραπάνω λίστες (Άσκσηση 6).
'''

#Ορίζουμε μια λίστα με τα ονόματα των αστεριών όπως δίνονται στον πίνακα.
stars = ['Σείριος','Εγγύτατος Κενταύρου','Αρκτούρος','Βέγας','Ρίγκελ']

#Ορίζουμε μια λίστα με τις αποστάσεις των 5 παραπάνω αστέρων (σε έτη φωτός):
distances = [8.6, 4.4, 37.0, 25.0, 860.]


#Ορίζουμε μια μεταβλητή που κρατάει την απόσταση του πλησιέστερου αστέρα.
#Η μεταβλητή αυτή χαρακτηρίζεται ως σημαία (flag) και της δίνουμε
#αρχική τιμή:
closest_dist = distances[0] #αντιστοιχεί σε 8.6

#############################################################

#Συγκρίνουμε έναν-έναν τους αστέρες να δούμε ποιος είναι ο πλησιέστερος.
#Όταν κάποιος αστέρας είναι πλησιέστερος του flag, τότε ανανεώνουμε
#τις τιμές της μεταβλητής closest_dist που δίνει την απόσταση και
#τη μεταβλητή closest_name που δίνει το όνομα.
#Είναι ο 1ος αστέρας o πλησιέστερος;
if distances[0]<closest_dist:
    closest_dist = distances[0]
    closest_name = stars[0]

#Είναι ο 2ος αστέρας o πλησιέστερος;
if distances[1]<closest_dist:
    closest_dist = distances[1]
    closest_name = stars[1]

#Είναι ο 3ος αστέρας o πλησιέστερος;
if distances[2]<closest_dist:
    closest_dist = distances[2]
    closest_name = stars[2]

#Είναι ο 4ος αστέρας o πλησιέστερος;
if distances[3]<closest_dist:
    closest_dist = distances[3]
    closest_name = stars[3]

#Είναι ο 5ος αστέρας o πλησιέστερος;
if distances[4]<closest_dist:
    closest_dist = distances[4]
    closest_name = stars[4]

#Ας δούμε ποιος είναι ο πλησιέστερος αστέρας από τους 5!
print('Ο πλησιέστερος αστέρας από τους πέντε είναι ο',closest_name,
      'σε απόσταση μόλις',closest_dist,'έτη φωτός από τη Γη!\n')

#############################################################
#############################################################

#Ακολουθούμε τώρα την ίδια λογική ψάχνοντας τον πιο απομακρυσμένο αστέρα
#από τη λίστα μας:
furthest_dist = distances[0] #αυτό αντιστοιχεί σε 8.6

#Είναι ο 1ος αστέρας o πιο απομακρυσμένος;
if distances[0]>closest_dist:
    furthest_dist = distances[0]
    furthest_name = stars[0]

#Είναι ο 2ος αστέρας o πιο απομακρυσμένος;
if distances[1]>closest_dist:
    furthest_dist = distances[1]
    furthest_name = stars[1]

#Είναι ο 3ος αστέρας o πιο απομακρυσμένος;
if distances[2]>closest_dist:
    furthest_dist = distances[2]
    furthest_name = stars[2]

#Είναι ο 4ος αστέρας o πιο απομακρυσμένος;
if distances[3]>closest_dist:
    furthest_dist = distances[3]
    furthest_name = stars[3]

#Είναι ο 5ος αστέρας o πιο απομακρυσμένος;
if distances[4]>closest_dist:
    furthest_dist = distances[4]
    furthest_name = stars[4]

#Ας δούμε ποιος είναι ο πιο απομακρυσμένος αστέρας από τους 5!
print('\nΟ πιο απομακρυσμένος αστέρας από τους πέντε είναι ο',furthest_name,
      'σε απόσταση',furthest_dist,'έτη φωτός από τη Γη!')

