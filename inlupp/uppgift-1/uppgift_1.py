# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd(x: int) -> bool:
    """
    is_odd är en funktion som returerar True om x är udda och False om x är jämnt.
    """
    if x % 2 != 0:
        return True
    else:
        return False
    
print(is_odd(11))
