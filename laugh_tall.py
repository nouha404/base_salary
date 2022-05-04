from selectors import BaseSelector


name = input('Votre nom : \n');
last_name = input('Votre prenom : \n');
year_of_birth = int(input("Votre année de naissance: \n"));
year_actualy = int(input("Entrez la date actuelle : \n"))

base_salary = int(input("Votre salaire de base : \n"));
statut_matrimonial = input(' Quel est votre situation : \n a : Celibataire \n b : Mariée \n c : Veuve \n d : Divorcée  \n');
gender = input('Votre sexe [ M ou F ] : \n');

question_child = input("Avez vous des enfants ? : \n");
number_child = "Indiquez le nombre d'enfants : \n"
response_for_nomber_child = int(input(number_child)) if question_child.lower() == 'oui' else '\n';

dure_of_staying = int(input("Nombre d'année excercer dans Laugh Tall ? \n"))
employer_post = input("Vous etes : [ a : directeur , b : vigile , c : retraité ] \n")

laugh_tall_taxe = 5/100;
etat_taxe = 18/100;
all_taxe = round(etat_taxe + laugh_tall_taxe, 2);
prime = 0;

if statut_matrimonial.lower() == 'b':
    prime += (2/100);
    if response_for_nomber_child == True:
        prime += number_child * (1/100);
        
elif gender.lower() == 'f' and dure_of_staying >= 3:
    prime += (2/100);
elif employer_post.lower() == 'a':
    prime += (2/100);
elif employer_post.lower() == 'b' and gender.lower() == 'f':
    prime += (5/100);
elif employer_post.lower() == 'c':
    base_salary += (35/100);
else:
    print("Pas de prime pour vous");
    
your_age = year_actualy - year_of_birth;
net_salary = (base_salary - all_taxe) + prime ;

print(f"{name.title()} {last_name.title()} vous avez {your_age} ans et votre salaire net apres les taxes est de : {round(net_salary, 2)} FCFA")

# Ecrire un programme qui permet de gerer les entreprises Laugh Tall .
# Le programme permet de saisir les données d'un employer puis de lui montrer son salaire nette.

# salaire nette = salaire de base + prime - taxe;

# Les données de l'employer sont :
#                                 nom, 
#                                 prenom, 
#                                 année de naissance, 
#                                 sa situation matrimoniale, 
#                                 son genre, 
#                                 nombre d'enfant, 
#                                 la durée de la personne dans l'entreprise ( ancienneté ) 
#                                 sa fonction,
# l'Etat prend 18% du salaire de l'employer (salaire de base) alors que l'entreprise elle meme prend 5% du salaire 
# base_salaire - 18/100
# net_salary - 5/100
# Les employés suivants on droit a des primes:
#                                             - 2% pour les marier 
#                                             - chaque enfants issue d'un employé marier a 1% 
# - Ya une prime d'edier au femme qui est de 0.5%  pour toute les femmes qui ont au moins durée 3 ans dans l'entreprise
# Les directeurs ont un prime de 2% Alors k les vigiles sexe feminin  5% 

# Les retraités ont un salaire  egale a 35% de leurs salaire de base  
# L'annéé en court est saisi par l'utilisateur .