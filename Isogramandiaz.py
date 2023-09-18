def je_isogram(iso):
    iso_cleaned = ''.join(char for char in iso if char.isalpha())
    iso_cleaned_lower = iso_cleaned.lower()

    is_isogram = len(iso_cleaned) == len(set(iso_cleaned_lower))

    return is_isogram, iso_cleaned_lower

def removeDigits(s):
    answer = []
    for char in s:
        if not char.isdigit():
            answer.append(char)
    return ''.join(answer)

result, cleaned_iso = je_isogram("")
if result:
    print(f'Reťazec "{cleaned_iso}" je isogram.')
else:
    print(f'Reťazec "{cleaned_iso}" nie je isogram.')



# answer = [] - Inicializuje prázdny zoznam answer, do ktorého budeme ukladať znaky, ktoré nie sú číslice
# return ''.join(answer) - Na konci funkcia použije metódu join na spojenie všetkých znakov v zozname answer späť do reťazca.
# def removeDigits(s): - Toto je funkcia názvom removeDigits. Táto funkcia prijíma jeden argument s, ktorý je reťazec, z ktorého chceme odstrániť všetky číslice.
# join je metóda reťazca v Pythone, ktorá slúži na spojenie (zreťazenie) viacerých reťazcov do jedného reťazca
# lower je metóda reťazca, ktorá prevedie všetky písmená v reťazci na malé písmená. Toto je užitočné pre porovnávanie reťazcov bez ohľadu na veľkosť písmen
# char je skratka pre "character" (znak) a v kontexte programovania sa používa na označenie jednotlivých znakov v reťazci. Reťazce sú zložené z množstva týchto znakov. Napríklad, ak máte reťazec "Hello", každé písmeno v tomto reťazci (t.j. "H", "e", "l", "l", "o") je znakom, a môžete s nimi pracovať samostatne alebo v skupinách v rámci vašeho programu. char je v tomto kontexte jednoducho premenná, ktorá reprezentuje jeden zo znakov vo vašom reťazci.
# set je ako krabica na hračky, do ktorej môžeš dať rôzne veci, ale každú vec môžeš dať tam iba raz. Krabica sama o sebe nemá žiadny špecifický poradie, a preto veci v nej nie sú usporiadané.
# len() je ako počítadlo, ktoré ti povie, koľko vecí máš v tvojej krabici na hračky.

 #   \n - nový řádek,

 #	\t - tabulátor,

 #	\a - zvonek (sekvecne pro pípnutí),

 #	\\ - zpětné lomítko se píše jako \\ ,
 #	protože jedním \ začínají speciální znaky,

 #	\' - jednoduché uvozovky,

 #	\" - dvojité uvozovky.

# Délku řetězce zjistíme pomocí funkce len():

# Slučování je spojení více řetězců do jednoho. Něco na způsob
# sčítání čísel. Jako operátor použijeme znaménko +:

