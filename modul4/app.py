# exerctiu 1
def fct_medie(lista_varste):
    return sum(lista_varste) / len(lista_varste)

def media_varste():
    lista = []
    nr_persoane = int(input('Cati participanti avem la sondaj?:'))
    for nr in range(nr_persoane):
        message = 'Introduceti varsta participantului '
        while True:
            try:
                varsta = int(input(f'{message} {nr + 1}:'))
                lista.append(varsta)
                break
            except ValueError:
                message = 'Reintroduceti varsta participantului'
                continue
    var = fct_medie(lista)
    print('Media de varsta a participantilo la sondaj este:', var)

media_varste()