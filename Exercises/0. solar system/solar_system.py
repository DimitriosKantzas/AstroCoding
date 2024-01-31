import random

def insert_planet():
    '''Επιλέγουμε έναν πλανήτη από το Ηλιακό σύστημα'''
    print('\nΓια ποιον πλανήτη θέλετε να μάθετε;\n\
    Επιλέξτε έναν από τη λίστα: \n ',*list_of_planets)
    planet = input()
    if planet in list_of_planets or planet in list_of_planets_no_stress:
        if planet in ['Ερμής','ερμής','ερμης','ΕΡΜΗΣ','ΕΡΜΉΣ']:
            planet = 'Ερμής'
        elif planet in ['Αφροδίτη','αφροδίτη','αφροδιτη','ΑΦΡΟΔΙΤΗ','ΑΦΡΟΔΊΤΗ']:
            planet = 'Αφροδίτη'
        elif planet in ['Γη','Γή','γή','γη','ΓΗ','ΓΉ']:
            planet = 'Γη'
        elif planet in ['Άρης','άρης','αρης','ΆΡΗΣ','ΑΡΗΣ']:
            planet = 'Άρης'
        elif planet in ['Δίας','δίας','διας','ΔΙΑΣ','ΔΪΑΣ']:
            planet = 'Δίας'
        elif planet in ['Κρόνος','κρόνος','κρονος','ΚΡΟΝΟΣ','ΚΡΌΝΟΣ']:
            planet = 'Κρόνος'
        elif planet in ['Ουρανός','ουρανός','ουρανος','ΟΥΡΑΝΟΣ','ΟΥΡΑΝΌΣ']:
            planet = 'Ουρανός'
        elif planet in ['Ποσειδώνας','ποσειδώνας','ποσειδωνας','ΠΟΣΕΙΔΩΝΑΣ','ΠΟΣΕΙΔΏΝΑΣ']:
            planet = 'Ποσειδώνας'
        print('\nΕπιλέξατε --- ',planet,' ---\n\n')
        return planet
    elif planet in ['Πωσειδόνας','πωσειδόνας','πωσειδονας','ΠΩΣΕΙΔΟΝΑΣ','ΠΩΣΕΙΔΌΝΑΣ']:
        answer = input('\nΜήπως εννοείται Ποσειδώνας; (y/n) ').lower()
        if answer in ['y','yes','υ']:
            planet = 'Ποσειδώνας'
            print('\nΕπιλέξατε --- ',planet,' ---\n\n')
            return planet
        else:
            return insert_planet()
    else:
        print(f'\nΧμμ... ίσως ο πλανήτης {planet} να μην ανήκει στο ηλιακό μας σύστημα! Δοκιμάστε από τη λίστα!\n')
        return insert_planet()

def insert_quantity():
    '''Επίλεγουμε ποια φυσική ποσότητα θέλουμε να μάθουμε από τον
    προς μελέτη πλανήτη'''
    print('Για ποια από τις παρακάτω φυσικές ποσότητες του πλανήτη θα θέλατε να μάθετε;\n\n\
        απόσταση από τον Ήλιο -- απόσταση\n\n\
        περίοδος περιφοράς    -- έτος\n\n\
        περίοδος περιστροφής  -- ημέρα\n\n\
        ακτίνα πλανήτη        -- ακτίνα\n\n\
        μάζα πλανήτη          -- μάζα\n\n\
        αριθμός δορυφόρων     -- δορυφόροι\n\n\
        βαρύτητα              -- βαρύτητα\n\n\
    (Επιλέξτε τη λέξη-κλειδί που βρίσκεται δεξιά της ποσότητας)')
    quantity = input().lower()
    if quantity in list_of_quantities or quantity in list_of_quantities_no_stress:
        print('\nEπιλέξατε --- ',quantity,' ---\n')
        return quantity
    else:
        print('\nΧμμ... ίσως δεν είναι ακόμα γνωστή αυτή η ποσότητα!\n')
        return insert_quantity()

def print_distance(distance_string,name,distance):
    '''Εκτυπώνει την απόσταση του πλανήτη'''
    print('\nH %s απόσταση του πλανήτη %s είναι %.2f AU από τον Ήλιο.\n\n'%(distance_string,name,distance))
    pass
    
def ask_for_distance(d_min,d_max,name):
    '''Επιλέγουμε ποια απόσταση θέλουμε min/max/mean'''
    distance_of_planet=input('Ποια απόσταση θέλετε να μάθετε;\n\
                             ελάχιστη, μέγιστη ή μέση;\n').lower()
    if distance_of_planet in ['ελάχιστη','ελαχιστη']:
        print_distance(distance_of_planet,name,d_min)
    elif distance_of_planet in ['μέγιστη','μεγιστη']:
        print_distance(distance_of_planet,name,d_max)
    elif distance_of_planet in ['μέση','μεση']:
        print_distance(distance_of_planet,name,(d_min+d_max)/2)
    else:
        print('Παρακαλώ επιλέξτε ελάχιστη, μέγιστη ή μέση!\n')
        ask_for_distance(d_min,d_max,name)
    pass
    
def ask_units_of_year(name,year_d):
    '''Επιλέγουμε τις μονάδες του έτους'''
    units_of_year = input('Θέλετε το έτος του πλανήτη σε -> ημέρες <-  ή -> έτη <- ;\n').lower()
    if units_of_year in ['ημέρες','ημερες']:
        print('\nΤο έτος του πλανήτη',name,'είναι {:.2f}'.format(year_d),'ημέρες\n\n')
    elif units_of_year in ['έτη','ετη']:
        print('\nΤο έτος του πλανήτη',name,'είναι {:.2f}'.format(year_d/yr_Earth),'έτη\n\n')
    else:
        print('\nΠαρακαλώ επιλέξτε ημέρες ή έτη!\n')
        ask_units_of_year(name,year_d)
    pass
    
def print_day(name,day,units):
    '''Εκτυπώνει την ημέρα του πλανήτη'''
    print('\nΗ ημέρα του πλανήτη',name,'είναι {:.2f}'.format(day),units,'\n\n')
    pass
def ask_units_of_day(name,day):
    '''Επιλέγουμε τις μονάδες της ημέρας'''
    units_of_day = input('Θέλετε την ημέρα του πλανήτη σε γήινες -> ημέρες <-  ή  -> ώρες <- ;\n').lower()
    if units_of_day in ['ημέρες','ημερες']:
        print_day(name,day,units_of_day)
    elif units_of_day in ['ώρες','ωρες']:
        print_day(name,day*24,units_of_day)
    else:
        print('\nΠαρακαλώ επιλέξτε ημέρες ή ώρες!\n')
        ask_units_of_day(name,day)
    pass

def new_quantity():
    '''Επιλέγουμε αν θέλουμε να εξετάσουμε νέα ποσότητα από τον ίδιο πλανήτη'''
    other_quant=\
      input('Θα θέλατε να μάθετε κάποια άλλη πληροφορία για αυτόν τον πλανήτη; (Υ/n)\n').lower()
    if other_quant in ['y','υ','yes']:
        return True
    elif other_quant in ['n','ν','no']:
        return False
    else:
        print('\nΠαρακαλώ επίλέξτε Y (yes=ναι) ή n (no=όχι)')
        return new_quantity()

def another_planet():
    '''Επιλέγουμε αν θέλουμε να εξετάσουμε έναν άλλον πλανήτη'''
    other_planet=\
      input('\nΘα θέλατε να μάθετε για κάποιον άλλον πλανήτη; (Υ/n)\n').lower()
    if other_planet in ['y','yes','υ']:
        return True
    elif other_planet in ['n','no','ν']:
        return False
    else:
        print('Παρακαλώ επίλέξτε Y (yes=ναι) ή n (no=όχι)')
        return another_planet()

def Kepler_third_law(distance,year_d):
    '''Εξετάζουμε τον 3ο νόμο του Kepler για τον υπο εξέταση πλανήτη'''
    all_choices  = ['α**3/T**2','α**2/T**3','α**2/T**2','α/T']
    random.shuffle(all_choices)
    print('\n\nΠοια από τις παρακάτω εκφράσεις είναι η σωστή διατύπωση του 3ου νόμου του Kepler;\n\n')
    for ind,choice in zip(['A.','B.','C.','D.'],all_choices):
        print(ind,choice,'\n')
    answer = input().lower()
    answer_list = ['a','b','c','d','α','β','1','2','3','4']
    if answer in answer_list:
        if answer in ['a','α','1']:
            answer_index = 0
        elif answer in ['b','β','2']:
            answer_index = 1
        elif answer in ['c','3']:
            answer_index = 2
        elif answer in ['d','4']:
            answer_index = 3
        if all_choices[answer_index]=='α**3/T**2':
            print('\n\tΣυγχαρητήρια! Σωστή απάντηση!\n')
            print('\nO 3ος νόμος του Kepler για αυτόν τον πλανήτη δίνει τιμή ίση με:\n\n \
                {:.2e}'.format(distance**3/year_d**2),' AU**3/day**2\n\n')
            return
        else:
            print('\n\tΚρίμα... λάθος απάντηση... Δεν πειράζει όμως! Δοκιμάστε ξανά!\n')
            return Kepler_third_law(distance,year_d)
    else:
        print(f'\n\tΟυπς δεν υπάρχει η απάντηση {answer} που προσπαθείτε να δώσετε...\n\
                    Δοκιμάστε ξανά!\n\n')
        return Kepler_third_law(distance,year_d)
        

def new_planet():
    '''Εξετάζουμε ένα νέο πλανήτη'''
    planet = insert_planet()
    
    Mercury={
        'ελάχιστη απόσταση':.31, #in AU
        'μέγιστη απόσταση':.47,
        'έτος': 87.97, #in Earth days
        'ημέρα': 58.65, #in Earth days
        'ακτίνα': .38, #in Earth radius
        'μάζα':.055, #in Earth mass
        'δορυφόροι':0,
        'βαρύτητα':.38 #in g=9.81m/s^2
    }
    Venus={
        'ελάχιστη απόσταση':0.72, #in AU
        'μέγιστη απόσταση':0.73,
        'έτος': 224.7,  #in Earth days
        'ημέρα':  243,#in Earth days
        'ακτίνα': 0.95,  #in Earth radius
        'μάζα': 0.82,  #in Earth mass
        'δορυφόροι':0,
        'βαρύτητα':0.9 #in g
    }
    Earth = {
        'ελάχιστη απόσταση':.98, #in AU
        'μέγιστη απόσταση':1.02,
        'έτος': 365.24,  #in Earth days
        'ημέρα':  1 ,#in Earth days
        'ακτίνα': 1,  #in Earth radius
        'μάζα': 1,  #in Earth mass
        'δορυφόροι':1,
        'βαρύτητα':1.0 #in g
    }
    Mars={
        'ελάχιστη απόσταση':1.38, #in AU
        'μέγιστη απόσταση':1.67 ,
        'έτος': 686.97, #in Earth days
        'ημέρα':  1.03 ,#in Earth days
        'ακτίνα': 0.53, #in Earth radius
        'μάζα':0.11, #in Earth mass
        'δορυφόροι':2,
        'βαρύτητα':.38 #in g
    }
    Jupiter={
        'ελάχιστη απόσταση': 5, #in AU
        'μέγιστη απόσταση': 5.5,
        'έτος': 11.862*365.24, #in Earth days
        'ημέρα':   9.925/24, #in Earth days
        'ακτίνα': 11, #in Earth radius
        'μάζα': 318,#in Earth mass
        'δορυφόροι': 79,
        'βαρύτητα': 2.528 #in g
    }
    Saturn ={
        'ελάχιστη απόσταση': 9, #in AU
        'μέγιστη απόσταση': 10,
        'έτος':  29.4571*365.24, #in Earth days
        'ημέρα':   10.55/24, #in Earth days
        'ακτίνα': 9, #in Earth radius
        'μάζα': 95.159,#in Earth mass
        'δορυφόροι': 82,
        'βαρύτητα': 1.065 #in g        
    }
    Uranus ={
        'ελάχιστη απόσταση': 18, #in AU
        'μέγιστη απόσταση': 20,
        'έτος':  84*365.24, #in Earth days
        'ημέρα':   17.23/24, #in Earth days
        'ακτίνα': 4, #in Earth radius
        'μάζα': 14.5,#in Earth mass
        'δορυφόροι': 27,
        'βαρύτητα': 0.866 #in g        
    }
    Neptune ={
        'ελάχιστη απόσταση': 29.81, #in AU
        'μέγιστη απόσταση': 30.33,
        'έτος':  164.8*365.24, #in Earth days
        'ημέρα':   16.1/24, #in Earth days
        'ακτίνα': 4, #in Earth radius
        'μάζα': 17.147,#in Earth mass
        'δορυφόροι': 14,
        'βαρύτητα': 1.14 #in g        
    }
    
    if  planet == 'Ερμής':
        planet_library = Mercury
    elif planet == 'Αφροδίτη':
        planet_library = Venus
    elif planet == 'Γη':
        planet_library = Earth
    elif planet == 'Άρης':
        planet_library = Mars
    elif planet == 'Δίας':
        planet_library = Jupiter
    elif planet == 'Κρόνος':
        planet_library = Saturn
    elif planet == 'Ουρανός':
        planet_library = Uranus
    elif planet == 'Ποσειδώνας':
        planet_library = Neptune
    else:
        print('Ουπς κάτι πήγε λάθος!')

    new_quant_flag = True
    while new_quant_flag:
        quantity = insert_quantity()
        if quantity in ['απόσταση','αποσταση']:
            ask_for_distance(planet_library['ελάχιστη απόσταση'],planet_library['μέγιστη απόσταση'],planet)
        elif quantity in ['έτος','ετος']:
            ask_units_of_year(planet,planet_library['έτος'])
        elif quantity in ['ημέρα','ημερα']:
            ask_units_of_day(planet,planet_library['ημέρα'])
        elif quantity in ['ακτίνα','ακτινα']:
            print('\nΗ ακτίνα του πλανήτη %s είναι %.2f γήινες ακτίνες.\n\n'%(planet,planet_library['ακτίνα']))
        elif quantity in ['μάζα','μαζα']:
            print('\nΗ μάζα του πλανήτη %s είναι %.2f γήινες μάζες.\n\n'%(planet,planet_library['μάζα']))
        elif quantity in ['δορυφόροι','δορυφοροι']:
            print('\nΟ πλανήτης %s έχει %i δορυφόρους.\n\n'%(planet,planet_library['δορυφόροι']))
        elif quantity in ['βαρύτητα','βαρυτητα']:
            print('\nΟ πλανήτης %s έχει %.2f τη γήινη βαρύτητα.\n\n'%(planet,planet_library['βαρύτητα']))
        else:
            print('Θα συμπληρώσουμε τις πληροφορίες σύντομα! Μείνετε συντονισμένοι!\n')

        new_quant_flag = new_quantity()
    else:
        print('\nΤέλεια! Μάθατε τόσο πολλά για αυτόν τον πλανήτη!\n\n')

    return planet_library

################################################################################
list_of_planets =['Ερμής','Αφροδίτη','Γη','Άρης','Δίας',
                  'Κρόνος','Ουρανός','Ποσειδώνας']
list_of_planets_no_stress =['ερμης','αφροδιτη','γη','αρης','διας',
                  'κρονος','ουρανος','ποσειδωνας']

list_of_quantities=['απόσταση','έτος','ημέρα','ακτίνα','μάζα','δορυφόροι','βαρύτητα']
list_of_quantities_no_stress=['αποσταση','ετος','ημερα','ακτινα','μαζα','δορυφοροι','βαρυτητα']

yr_Earth = 365.0

if __name__ == '__main__':
    print('\nΓΝΩΡΙΣΤΕ ΤΟΥΣ ΠΛΑΝΗΤΕΣ!\n\n')
    new_planet_flag = True

    while new_planet_flag:
        planet_lib= new_planet()

        print('\nΘέλετε να μάθετε για τον 3ο νόμο του Kepler για αυτόν τον πλανήτη; Υ/n\n')
        K3l = input().lower()
        K3l_flag = True if K3l in ['y','yes','υ'] else False
        if K3l_flag:
            Kepler_third_law((planet_lib['ελάχιστη απόσταση']+planet_lib['μέγιστη απόσταση'])/2,planet_lib['έτος'])

        new_planet_flag = another_planet()
    else:
        print('\nΜάθατε σχεδόν τα πάντα για τους πλανήτες! Μπράβο!\n\n')

    print('Ευχαριστούμε που μάθατε για τους πλανήτες παίζοντας με την Python!\n\n\
          Εις το επανιδείν!\n\n')  
################################################################################