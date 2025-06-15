def calculate1(a, b, operateur):
    """
    Effectue une opération mathématique entre deux nombres.

    Paramètres :
    a (float | int) : le premier nombre
    b (float | int) : le second nombre
    operateur (str) : un des opérateurs suivants '+', '-', '*', '/'

    Retourne :
    Le résultat de l'opération si l'opérateur est valide.
    Affiche un message d'erreur en cas de division par zéro ou d'opérateur invalide.
    """
    if operateur == '+':
        return a + b
    elif operateur == '-':
        return a - b
    elif operateur == '*':
        return a * b
    elif operateur == '/':
        if b == 0:
            return "Erreur : division par zéro"
        return round(a / b, 2)
    else:
        return "Erreur : opérateur non valide"
    
def calculate2(a, b, op):
    """
    Effectue une opération mathématique entre deux entiers.

    Paramètres :
    a (int) : le premier entier
    b (int) : le second entier
    op (str) : une chaîne représentant l'opération à effectuer, parmi '+', '-', '*', '/'

    Retour :
    float | int : le résultat de l'opération (arrondi à 2 décimales en cas de division)
    
    Exceptions :
    - Soulève une ZeroDivisionError si b == 0 et op == '/'
    - Soulève une ValueError si l'opérateur est invalide
    """

    # Vérifie l'opérateur et effectue l'opération correspondante
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division par zéro interdite.")
        return round(a / b, 2)
    else:
        raise ValueError(f"Opérateur invalide : '{op}'. Utilisez '+', '-', '*' ou '/'.")

def calculate3(a, b, op):
    """
    Effectue une opération mathématique entre deux entiers.

    Args:
        a (int): Le premier entier.
        b (int): Le second entier.
        op (str): L'opérateur mathématique à appliquer ('+', '-', '*', '/').

    Returns:
        float | int: Le résultat de l’opération.
                     La division est arrondie à deux décimales.

    Raises:
        ZeroDivisionError: Si une division par zéro est tentée.
        ValueError: Si l’opérateur est invalide.
    """
    # Vérification et exécution selon l’opérateur
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Erreur : division par zéro.")
        return round(a / b, 2)
    else:
        raise ValueError(f"Erreur : opérateur non reconnu '{op}'. Utilisez '+', '-', '*', ou '/'.")
# LES FONCTIONS DU DEUXIEMES EXERCICE :
def format_product_code(product_id):
    """
    Formate un identifiant produit en y insérant des tirets après le 3e et le 7e caractère.

    Args:
        product_id (str): Une chaîne alphanumérique de 10 caractères.

    Returns:
        str: L'identifiant formaté sous la forme 'XXX-XXXX-XXX'.

    Raises:
        ValueError: Si la chaîne n'a pas exactement 10 caractères
                    ou contient des caractères non alphanumériques.
    """
    if not isinstance(product_id, str):
        raise ValueError("Le product_id doit être une chaîne de caractères.")

    if len(product_id) != 10:
        raise ValueError("Le product_id doit contenir exactement 10 caractères.")

    if not product_id.isalnum():
        raise ValueError("Le product_id doit être alphanumérique (lettres et chiffres uniquement).")

    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"

def format_product_code1(product_id):
    """
    Formate un identifiant produit alphanumérique de 10 caractères
    en insérant des tirets après le 3e et le 6e caractère.

    Exemple :
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'

    Args:
        product_id (str): Identifiant produit alphanumérique de 10 caractères.

    Returns:
        str: L'identifiant formaté sous la forme 'XXX-XXX-XXXX'.

    Raises:
        ValueError: Si product_id n'est pas une chaîne de 10 caractères alphanumériques.
    """
    if not isinstance(product_id, str):
        raise ValueError("L'identifiant doit être une chaîne de caractères.")

    if len(product_id) != 10:
        raise ValueError("L'identifiant doit contenir exactement 10 caractères.")

    if not product_id.isalnum():
        raise ValueError("L'identifiant doit être strictement alphanumérique.")

    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"

def format_product_code2(product_id):
    """
    Formate un identifiant produit alphanumérique de 10 caractères
    en insérant des tirets après le 3e et le 6e caractère.

    Format attendu : 'XXX-XXX-XXXX'

    Exemples :
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'

        >>> format_product_code("XYZ987GHIJ")
        'XYZ-987-GHIJ'

        >>> format_product_code("SHORT")
        ValueError: L'identifiant doit contenir exactement 10 caractères.

    Args:
        product_id (str): Une chaîne alphanumérique de 10 caractères.

    Returns:
        str: L'identifiant formaté.

    Raises:
        ValueError: Si l'entrée n'est pas une chaîne alphanumérique de 10 caractères.
    """
    if not isinstance(product_id, str):
        raise ValueError("L'identifiant doit être une chaîne de caractères.")

    if len(product_id) != 10:
        raise ValueError("L'identifiant doit contenir exactement 10 caractères.")

    if not product_id.isalnum():
        raise ValueError("L'identifiant doit être strictement alphanumérique.")

    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"
