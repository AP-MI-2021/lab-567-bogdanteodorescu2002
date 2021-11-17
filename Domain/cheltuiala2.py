def creeaza_cheltuiala(id: int, nr_ap: int, suma: float, data: str, tipul: str):
    """
    Creeaza o cheltuiala.
    :param id: id cheltuiala unic
    :param nr_ap: Numarul unui apartament, nenul
    :param suma: suma de plata
    :param data: Data din calendar
    :param tipul: tipul cheltuielilor
    :return: o cheltuiala de proprietar
    """
    return{
        'id': id,
        'nr': nr_ap,
        'suma': suma,
        'data': data,
        'tipul': tipul,
    }


def get_id_cheltuiala(cheltuiala):
    """
    Getter-ul pentru id-ul cheltuielii
    :param cheltuiala: cheltuiala
    :return: id-ul cheltuielii date ca parametru
    """
    return cheltuiala['id']


def get_nr_apartament(cheltuiala):
    """
    Getter-ul pentru numarul apartamentului
    :param cheltuiala: cheltuiala
    :return: numarul apartamentului cheltuielii date ca parametru
    """
    return cheltuiala['nr']


def get_suma(cheltuiala):
    """
    Getter-ul pentru suma de plata
    :param cheltuiala: cheltuiala
    :return: suma de plata a cheltuielii
    """
    return cheltuiala['suma']


def get_data(cheltuiala):
    """
    Getter-ul de data
    :param cheltuiala: cheltuiala
    :return: data emiterii unei cheltuieli
    """
    return cheltuiala['data']


def get_tipul(cheltuiala):
    """
    Getter-ul tipului de cheltuiala
    :param cheltuiala: cheltuiala
    :return: tipul de cheltuiala
    """
    return cheltuiala['tipul']


def get_str(cheltuiala):
    return f'Cheltuiala cu id-ul {get_id_cheltuiala(cheltuiala)}, a apartamentului {get_nr_apartament(cheltuiala)}, emisa la data {get_data(cheltuiala)}, in valoare de {get_suma(cheltuiala)}, pentru {get_tipul(cheltuiala)}'