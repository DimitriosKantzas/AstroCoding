#Ορίζουμε πρώτα τις σταθερές του προβλήματος:
AU = 149*10**6              #Astronomical Unit= μέση απόσταση Γης-Ήλιου σε km
c = 300000                  #Ταχύτητα φωτός σε km/s

#Ορίζουμε τις μεταβλητές του προβλήματος:
d_Earth = 1.0*AU            #Η απόσταση Γης-Ήλιου
d_Mars_Earth_min = 0.5*AU   #Η ελάχιστη απόσταση Άρη-Γης
d_Mars_Earth_max = 2.5*AU   #Η μέγιστη απόσταση Άρη-Γης

#Εαν ο πλανήτης Άρης βρίσκεται στην ελάχιστη απόσταση από τη Γη,
#τύπωσε το χρόνο που κάνει το φως να φτάσει από τον Άρη στη Γη:
time_min = d_Mars_Earth_min/c/60
#print('Ο χρόνος που απαιτείται είναι',time_min,'λεπτά')

#Εαν ο πλανήτης Άρης βρίσκεται στη μέγιστη απόσταση από τη Γη,
#τύπωσε το χρόνο που κάνει το φως να φτάσει από τον Άρη στη Γη:
time_max = d_Mars_Earth_max/c/60
#print('Ο χρόνος που απαιτείται είναι',time_max,'λεπτά')


n = 3       #Ορίζουμε έναν τυχαίο αριθμό μεταξύ 0 και 10
#Θέλουμε να δούμε αν ο αριθμός αυτός είναι μεγαλύτερος του 5
if n>5:
    print('Ο αριθμός',n, 'είναι μεγαλύτερος του 5!')

n = 6       #Ορίζουμε έναν τυχαίο αριθμό μεταξύ 0 και 10
#Θέλουμε να δούμε αν ο αριθμός αυτός είναι μεγαλύτερος του 5
if n>5:
    print('Ο αριθμός',n, 'είναι μεγαλύτερος του 5!')
