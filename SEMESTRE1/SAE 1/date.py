# %%
# # Implémentation des dates et calendriers
# Implémentation des tests (voir main en fin de fichier)

from typing import Dict, List, Tuple, NoReturn

type_affichage = 'FR'


# =============================================================================
def est_bissextile(annee: int) -> bool:
    if annee % 400 == 0:
        return True
    elif annee % 4 == 0 and annee % 100 != 0:
        return True
    else:
        return False


# =============================================================================
def cree_date(j: int, m: int, a: int) -> Dict:
    """
    Crée une date à partir des entiers la décrivant.
    Si l'un des paramètres n'est pas un entier, la fonction retournera None

    >>> cree_date(15,12,2020)
    {'jour': 15, 'mois': 12, 'annee': 2020}
    >>> cree_date(1.5,12,2020) is None
    True
    """
    if type(j) is int and type(m) is int and type(a) is int:
        date = {'jour': j, 'mois': m, 'annee': a}
        return date
    else:
        return None


# =============================================================================
def copie_date(date: Dict) -> Dict:
    """
    copie la date passée en paramètre
    """
    date_copie = date.copy()
    return date_copie


# =============================================================================
def compare(d1: Dict, d2: Dict) -> int:
    """
    Permet de classer deux dates.
    Retourne
    -1 si la date d1 < d2
    +1 si la date d1 > d2
    0 si les dates sont identiques
    on considère que les dates sont croissantes
    dans l'ordre chronologique

    >>> date1 = cree_date(25,12,2021)
    >>> date2 = cree_date(31,12,2021)
    >>> compare(date1,date2)
    -1
    >>> compare(date2,date1)
    1
    >>> compare(date1,date1)
    0
    """
    if d1['annee'] == d2['annee']:
        if d1['mois'] == d2['mois']:
            if d1['jour'] == d2['jour']:
                return 0
            elif d1['jour'] < d2['jour']:
                return -1
            else:
                return 1
        elif d1['mois'] < d2['mois']:
            return -1
        else:
            return 1
    elif d1['annee'] < d2['annee']:
        return -1
    else:
        return 1

# =============================================================================


def valide_simple(d: Dict) -> bool:
    """
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - si le premier (le jour) est un entier compris entre 1 et 31
    - si le second (le mois) est un entier compris entre 1 et 12

    >>> date = cree_date(1, 2, 0)
    >>> valide_simple(date)
    True
    >>> date = cree_date(1.5, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(0, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(20, 8, 2021)
    >>> valide_simple(date)
    True
    """
    if d == None:
        return False
    elif 1 <= d['mois'] <= 12 and 1 <= d['jour'] <= 31:
        return True
    else:
        return False


# =============================================================================
def valide_complet(d: Dict) -> bool:
    """
        retourne vrai si la date est valide.
        on supposera que la date est valide si :
        - la validation simple est vraie
        - si la date représente une date réelle

        >>> date = cree_date(15, 1, 2022)
        >>> valide_complet(date)
        True
        >>> date = cree_date(32, 1, 2022)
        >>> valide_complet(date)
        False
        >>> date = cree_date(-1, 1, 2022)
        >>> valide_complet(date)
        False
        >>> date = cree_date(31, 6, 2022)
        >>> valide_complet(date)
        False
        >>> date = cree_date(29, 2, 2020)
        >>> valide_complet(date)
        True
        >>> date = cree_date(29, 2, 2022)
        >>> valide_complet(date)
        False
        """
    if valide_simple(d) == True:

        if d['mois'] == 4 or d['mois'] == 6 or d['mois'] == 9 or d['mois'] == 11:

            if d['jour'] == 31:
                return False
            else:
                return True
        elif est_bissextile(d['annee']) == True:

            if 1 <= d['jour'] <= 29:
                return True
            else:
                return False

        elif est_bissextile(d['annee']) == False:
            if 1 <= d['jour'] <= 28:
                return True
            else:
                return False

        else:
            return False
    else:
        return False


# =============================================================================
def ajoute_calendrier(calendrier: List, date: Dict, description: str) -> NoReturn:
    """Procédure qui ajoute une date a un calendrier et une description (paque,noel,etc)
        >>> calendrier=[]
        >>> date = cree_date(21,12,2020)
        >>> description = 'noel'
        >>> ajoute_calendrier(calendrier,date,description)
    """
    calendrier.append([date, description])


# =============================================================================
def affiche_calendrier(calendrier: List) -> NoReturn:
    """
    >>> calendrier=[]
    >>> ajoute_calendrier ( calendrier , cree_date (1 ,1 ,2022) ,' Jour de l ’an ' )
    >>> ajoute_calendrier ( calendrier , cree_date (1 ,5 ,2022) , 'Fête du travail ' )
    >>> ajoute_calendrier ( calendrier , cree_date (8 ,5 ,2022) , ' Armistice 1945 ' )
    >>> ajoute_calendrier ( calendrier , cree_date (14 ,7 ,2022) , ' Fête nationale ' )
    >>> ajoute_calendrier ( calendrier , cree_date (15 ,8 ,2022) , ' Assomption ' )
    >>> ajoute_calendrier ( calendrier , cree_date (25 ,12 ,2022) , ' Noel ' )

    >>> affiche_calendrier(calendrier)
    Le 1/1/2022 : Jour de l'an
    Le 1/5/2022 : Fête du travail
    Le 8/5/2022 : Armistice 1945
    Le 14/7/2022 : Fête nationale
    Le 25/8/2022 : Assomption
    Le 25/12/2022 : Noel
    """
    longueur_calendrier = len(calendrier)
    if type_affichage == 'FR':
        for i in range(longueur_calendrier):
            print('Le ', calendrier[i][0].get('jour'), '/', calendrier[i][0].get(
                'mois'), '/', calendrier[i][0].get('annee'), ' : ', calendrier[i][1])
    elif type_affichage == 'GB':
        for i in range(longueur_calendrier):
            print('Le ', calendrier[i][0].get('mois'), '/', calendrier[i][0].get(
                'jour'), '/', calendrier[i][0].get('annee'), ' : ', calendrier[i][1])
    else:
        print(' ce format n\'existe pas ')


def format_affichage(affichage: str) -> NoReturn:
    global type_affichage
    type_affichage = affichage


def calcule_jour(date: dict) -> str:
    """
    >>> date1 = cree_date(1,2,2020)
    >>> date2 = cree_date(2,2,2020)
    >>> date3 = cree_date(3,2,2020)
    >>> date4 = cree_date(4,2,2020)
    >>> date5 = cree_date(30,2,2020)
    >>> print(calcule_jour(date1))
    >>> print(calcule_jour(date2))
    >>> print(calcule_jour(date3))
    >>> print(calcule_jour(date4))
    >>> print(calcule_jour(date5)) 
    Samedi
    Dimanche
    Lundi
    Mardi
    la date n'est pas ok
    """

    if valide_complet(date) == True:
        if date.get('mois') < 3:
            numero_du_jour = ((23*date.get('mois'))/9 + date.get('jour') + 4 + date.get('annee') + (
                (date.get('annee') - 1)/4) - ((date.get('annee') - 1)/100) + (date.get('annee') - 1) / 400) % 7
            if round(numero_du_jour) == 1:
                return 'Dimanche'
            if round(numero_du_jour) == 2:
                return 'Lundi'
            if round(numero_du_jour) == 3:
                return 'Mardi'
            if round(numero_du_jour) == 4:
                return 'Mercredi'
            if round(numero_du_jour) == 5:
                return 'Jeudi'
            if round(numero_du_jour) == 6:
                return 'Vendredi'
            if round(numero_du_jour) == 7:
                return 'Samedi'
            
        else:
            numero_du_jour = (((23*date.get('mois'))/9) + date.get('jour') + 2 + date.get('annee') + (
                (date.get('annee'))/4) - (date.get('annee')/100) + (date.get('annee')/400)) % 7
            if round(numero_du_jour) == 1:
                return 'Dimanche'
            if round(numero_du_jour) == 2:
                return 'Lundi'
            if round(numero_du_jour) == 3:
                return 'Mardi'
            if round(numero_du_jour) == 4:
                return 'Mercredi'
            if round(numero_du_jour) == 5:
                return 'Jeudi'
            if round(numero_du_jour) == 6:
                return 'Vendredi'
            if round(numero_du_jour) == 7:
                return 'Samedi'
    else:
        return 'la date n\'est pas ok '


def calcule_veille_lendemain(date: Dict) -> Tuple[Dict, Dict]:
    # toutes les exeptions: si c'est la fin ou le début du mois il faut retourner d'un mois et mettre le dernier jour. Fin d'année changez d'année. Mois bissextile. sois là ou on est soit la ou on serrat.

    # ---------------------------------------------------------------------------------------------------------------------------------
    # __ On vérifie le cas général ou il faudrat simplement descendre d'un jour.
    if 1 < date['jour'] < 28 and 1 < date.get('mois') < 12:
        date_veille = date.copy()
        date_veille['jour'] = date_veille['jour'] - 1
        date_lendemain = date.copy()
        date_lendemain['jour'] = date_lendemain['jour'] + 1

    # __ On prend le cas ou on est en février et si le jour est 29 bissextile ou 28 bissextile. Là ou c'est l'extrémité et donc il faudrat passer a l'autre mois.

    elif date['jour'] == 29 and date.get('mois') == 2 and est_bissextile(date['annee']) == True or date['jour'] == 28 and date.get('mois') == 2 and est_bissextile(date['annee']) == False:

        date_veille = date.copy()
        date_veille['jour'] = date_veille['jour'] - 1
        date_lendemain = date.copy()
        date_lendemain['jour'] = 1
        date_lendemain['mois'] = date_lendemain['mois'] + 1
    elif est_bissextile(date['jour']) == True and 1 < date['jour'] < 29 or est_bissextile(date['jour']) == False and 1 < date['jour'] < 28:

        date_veille = date.copy()
        date_veille['jour'] = date_veille['jour'] - 1
        date_lendemain = date.copy()
        date_lendemain['jour'] = date_lendemain['jour'] + 1

    elif date['jour'] == 1 and date.get('mois') == 3:
        if est_bissextile(date['annee']) == False:
            date_lendemain = date.copy()
            date_lendemain['jour'] += 1
            date_veille = date.copy()
            date_veille['jour'] = 28
            date_veille['mois'] = date_veille['mois'] - 1
        else:
            date_lendemain = date.copy()
            date_lendemain['jour'] += 1
            date_veille = date.copy()
            date_veille['jour'] = 29
            date_veille['mois'] = date_veille['mois'] - 1
    elif 1 < date['jour'] < 31 and date.get('mois') == 3:

        date_veille = date.copy()
        date_veille['jour'] = date_veille['jour'] - 1
        date_lendemain = date.copy()
        date_lendemain['jour'] = date_lendemain['jour'] + 1

    elif date.get('mois') == 3 and date['jour'] == 31:

            date_lendemain = date.copy()
            date_lendemain['jour'] = 1
            date_lendemain['mois'] = date_lendemain['mois'] + 1
            date_veille = date.copy()
            date_veille['jour'] = 29

        # __ On prend le cas ou on le jour est 30 qui est l'extremité de quelques mois.

    elif date['jour'] == 30:

        """ ___ On vérifie si c'est le mois 4,6 ou 9 [qui sont les mois avec 30 jour ]."""

        if date.get('mois') == 4 or date.get('mois') == 6 or date.get('mois') == 9 or date.get('mois') == 11:

            """ on creer une copie pour changer les jour selons les règles et leurs placement. """

            date_veille = date.copy()
            date_veille['jour'] = date_veille['jour']-1
            date_lendemain = date.copy()
            date_lendemain['jour'] = 1
            date_lendemain['mois'] = date_lendemain['mois'] + 1

        elif date.get('mois') == 1 or date.get('mois') == 5 or date.get('mois') == 7 or date.get('mois') == 8 or date.get('mois') == 10 or date.get('mois') == 12:

            """ ___ On vérifie si c'est le mois 4,6 ou 9 [qui sont les mois avec 31 jour ]. """

            date_veille = date.copy()
            date_veille['jour'] = date_veille['jour']-1
            date_lendemain = date.copy()
            date_lendemain['jour'] = date_lendemain['jour']+1

    elif date['jour'] == 31:

        if date.get('mois') == 1 or date.get('mois') == 5 or date.get('mois') == 7 or date.get('mois') == 8 or date.get('mois') == 10:

            """ __ On vérifie si c'est le mois 4, 6, ou 9 [qui sont les mois avec 31 jour] """

            date_veille = date.copy()
            date_veille['jour'] = date_veille['jour'] - 1
            date_lendemain = date.copy()
            date_lendemain['jour'] = date_lendemain['jour'] + 1
            date_lendemain['mois'] = date_lendemain['mois'] + 1

        elif date.get('mois') == 12:
            """on vérifie le cas où c'est le mois est 12"""
            date_veille = date.copy()
            date_veille['jour'] = date_veille['jour'] - 1
            date_lendemain = date.copy()
            date_lendemain['jour'] = 1
            date_lendemain['mois'] = 1
            date_lendemain['annee'] = date_lendemain['annee'] + 1

    # __ On prend le cas ou on est au début du mois car il faut reculer d'un mois.
    # 31 = [3,5,7,8,10]
    # 30 = [4,6,9,11]
    # 28,29 = [2]

    elif date['jour'] == 1:
        """ On vérifie le cas ou on est le premier qui est  """
        if date.get('mois') == 5 or date.get('mois') == 7 or date.get('mois') == 10 or date.get('mois') == 12:

            date_veille = date.copy()
            date_veille['jour'] = 30
            date_veille['mois'] = date_veille['mois'] - 1
            date_lendemain = date.copy()
            date_lendemain['jour'] = date_lendemain['jour'] + 1

        elif date.get('mois') == 8:

            date_veille = date.copy()
            date_veille['jour'] = 31
            date_veille['mois'] = date_veille['mois']-1
            date_lendemain = date.copy()
            date_lendemain['jour'] = date_lendemain['jour']+1

        elif date.get('mois') == 4 or date.get('mois') == 6 or date.get('mois') == 9 or date.get('mois') == 11:

            date_veille = date.copy()
            date_veille['jour'] = 31
            date_veille['mois'] = date_veille['mois']-1
            date_lendemain = date.copy()
            date_lendemain['jour'] = date_lendemain['jour'] + 1

        elif date.get('mois') == 1:

            date_veille = date.copy()
            date_veille['jour'] = 1
            date_veille['mois'] = 12
            date_veille['annee'] = date_veille['annee'] - 1
            date_lendemain = date.copy()
            date_lendemain['jour'] = date_lendemain['jour'] + 1

        else:
            return ' je sais pas '
    else:
        return 'je sais '
    return [date_veille, date_lendemain]


def ajoute_n_jour(date: Dict, n: int) -> Dict:

    # Le chiffre ne peut pas être négatif car les jour aussi ne peuvent pas l'être.

    if n > 0:
        #
        if date.get('mois') == 4 or date.get('mois') == 6 or date.get('mois') == 9 or date.get('mois') == 11:

            if date.get('jour')+n < 30:
                date['jour'] = date.get('jour') + n
                return date

            # date.get('jour') + n correspond au mois au jour restant après
            elif date.get('jour') + n >= 30:
                # date.get('jour')+n // 30 correspond au mois qui serront ajouté. et date.get('jour') + n % 30 correspond au jour restant apres être passer par les mois.
               # si les mois a ajouté sont inférieur au mois d'une année.
               if (date.get('jour') + n) // 30 < 12:
                # On change alors la valeurs des mois car il peuvent changer sans monter en année
                    date['mois'] = date.get('mois') + ((date.get('jour') + n) // 30)
                    # 31 = [3,5,8,10] Exception pour le mois " 7 " car si le mois d'après est 8 il y'a 31 jour
                    # 30 = [4,6,9,11]
                    # 28,29 = [2]
                    if date.get('mois') == 1 or date.get('mois') == 3 or date.get('mois') == 5 or date.get('mois') == 8 or date.get('mois') == 10 or date.get('mois') == 7 or date.get('mois') == 12 :
                        #Si on est dans un mois a 30 jour le jour doit avoir <=30 jour. 
                        date['jour'] = ((date.get('jour') + n) % 31)
                        return date

                    elif  date.get('mois') == 4 or date.get('mois') == 6 or date.get('mois') == 9 or date.get('mois') == 11:
                        #Si c'est un mois qui a 31 jour le jour doit avoir  <= 31 jour. 
                        date['jour'] =(date.get('jour') + n) % 30
                        return date

                    elif date.get('mois') == 2 and est_bissextile(date['annee'])== False:
                        #Si on est dans le mois de Février et une annee non bissextile les jour ne doivent pas dépasser 28 jour.
                        date['jour'] = (date.get('jour') + n % 28)
                        return date

                    elif date.get('mois') == 2 and est_bissextile(date['annee'])== True:
                        # Si on est dans le mois de Février et une annee bissextile les jour ne doivent pas dépasser 29 jour. 
                        date['jour'] =  (date.get('jour') + n % 29)
                        return date      

                # 31 = [3,5,7,8,10]
        elif date.get('mois') == 1 or date.get('mois') == 3 or date.get('mois') == 5 or date.get('mois') == 7 or date.get('mois') == 8 or date.get('mois') == 10 or date.get('mois') == 12 :

            if date.get('jour')+n < 31:
                date['jour'] = date.get('jour') + n
                return date

            # date.get('jour') + n correspond au mois au jour restant après
            elif date.get('jour') + n >= 31:
                # date.get('jour')+n // 30 correspond au mois qui serront ajouté. et date.get('jour') + n % 30 correspond au jour restant apres être passer par les mois.
               # si les mois a ajouté sont inférieur au mois d'une année.
               if (date.get('jour') + n) // 31 < 12:
                # On change alors la valeurs des mois car il peuvent changer sans monter en année
                    date['mois'] = date.get('mois') + ((date.get('jour') + n) // 31)
                    # 31 = [3,5,8,10] Exception pour le mois " 7 " car si le mois d'après est 8 il y'a 31 jour
                    # 30 = [4,6,9,11]
                    # 28,29 = [2]
                    if date.get('mois') == 1 or date.get('mois') == 3 or date.get('mois') == 5 or date.get('mois') == 8 or date.get('mois') == 10 or date.get('mois') == 7 or date.get('mois') == 12 :
                        #Si on est dans un mois a 30 jour le jour doit avoir <=30 jour. 
                        date['jour'] = ((date.get('jour') + n) % 31)
                        return date

                    elif  date.get('mois') == 4 or date.get('mois') == 6 or date.get('mois') == 9 or date.get('mois') == 11:
                        #Si c'est un mois qui a 31 jour le jour doit avoir  <= 31 jour. 
                        date['jour'] =(date.get('jour') + n) % 30
                        return date

                    elif date.get('mois') == 2 and est_bissextile(date['annee'])== False:
                        #Si on est dans le mois de Février et une annee non bissextile les jour ne doivent pas dépasser 28 jour.
                        date['jour'] = (date.get('jour') + n % 28)
                        return date

                    elif date.get('mois') == 2 and est_bissextile(date['annee'])== True:
                        # Si on est dans le mois de Février et une annee bissextile les jour ne doivent pas dépasser 29 jour. 
                        date['jour'] =  (date.get('jour') + n % 29)
                        return date
                
        elif date.get('mois')== 2 and est_bissextile(date.get('annee')) == True:

            if date.get('jour')+n < 29:
                date['jour'] = date.get('jour') + n
                return date

            # date.get('jour') + n correspond au mois au jour restant après
            elif date.get('jour') + n >= 29:
                # date.get('jour')+n // 30 correspond au mois qui serront ajouté. et date.get('jour') + n % 30 correspond au jour restant apres être passer par les mois.
               # si les mois a ajouté sont inférieur au mois d'une année.
               if (date.get('jour') + n) // 29 < 12:
                # On change alors la valeurs des mois car il peuvent changer sans monter en année
                    date['mois'] = date.get('mois') + ((date.get('jour') + n) // 29)
                    # 31 = [3,5,8,10] Exception pour le mois " 7 " car si le mois d'après est 8 il y'a 31 jour
                    # 30 = [4,6,9,11]
                    # 28,29 = [2]
                    if date.get('mois') == 1 or date.get('mois') == 3 or date.get('mois') == 5 or date.get('mois') == 8 or date.get('mois') == 10 or date.get('mois') == 7 or date.get('mois') == 12 :
                        #Si on est dans un mois a 30 jour le jour doit avoir <=30 jour. 
                        date['jour'] = ((date.get('jour') + n) % 31)
                        return date

                    elif  date.get('mois') == 4 or date.get('mois') == 6 or date.get('mois') == 9 or date.get('mois') == 11:
                        #Si c'est un mois qui a 31 jour le jour doit avoir  <= 31 jour. 
                        date['jour'] =(date.get('jour') + n) % 30
                        return date

                    elif date.get('mois') == 2 and est_bissextile(date['annee'])== False:
                        #Si on est dans le mois de Février et une annee non bissextile les jour ne doivent pas dépasser 28 jour.
                        date['jour'] = (date.get('jour') + n % 28)
                        return date

                    elif date.get('mois') == 2 and est_bissextile(date['annee'])== True:
                        # Si on est dans le mois de Février et une annee bissextile les jour ne doivent pas dépasser 29 jour. 
                        date['jour'] =  (date.get('jour') + n % 29)
                        return date

        else:
            return 'je ne reconnais pas le mois'
    else:
        return 'pas > 0'

def ajoute_fetes ( calendrier : List , annee : int ) -> NoReturn :
    ajoute_calendrier(calendrier,cree_date(1,2,annee), 'Jour de l\'an')
    ajoute_calendrier(calendrier,cree_date(1,5,annee), 'Fête du travail')
    ajoute_calendrier(calendrier,cree_date(8,5,annee), 'Armistice 1945')
    ajoute_calendrier(calendrier,cree_date(14,7,annee), 'Fête nationale ')
    ajoute_calendrier(calendrier,cree_date(25,8,annee), 'Assomption')
    ajoute_calendrier(calendrier,cree_date(25,12,annee), 'Noel')


def trouve_evenement ( calendrier : List , date : Dict ) -> str :
    trouver = False
    i=0
    while not trouver and i<len(calendrier):
        if calendrier[i][0]== date:
            trouver = True
            return calendrier[i][1]
        else:
            trouver = False
            i += 1
        if i == len(calendrier):
            return 'la date n\'existe pas '

    
        

    
#=============================================================================
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


# %%
