#code source
#tests unitaires pour la méthode compute_rules

def compute_rules(neighs_value, local_value):
# code à faire ici: les règles du jeu de la vie

from codesource import compute_rules

assert compute_rules([1,0,0,0,1,0,1,0], 0) == 1 #test règle 1 naissance
assert compute_rules([1,0,0,0,0,0,1,0], 1) == 1 #test règle 2 reste en vie
assert compute_rules([1,0,0,0,0,1,1,0], 1) == 1 #test règle 2 reste en vie
assert compute_rules([0,0,0,1,0,0,0,0], 1) == 0 #test règle 3 isolement
assert compute_rules([0,0,1,1,1,0,1,0], 1) == 0 #test règle 3 surpeuplement
assert compute_rules([1,0,0] , 1) == 0 #test règle 3 isolement pour un bord/coin
assert compute_rules([6,0,1,1,1,0,1,0], 1) == NA #valeur abérrante
assert compute_rules([0,0,1,1,1,0,-1,0], 1) == NA #valeur négative
assert compute_rules([0.0,0.1,1.237,1.0,1.0,0.4,1.3,0.2], 1) == 0 #avec des floats
