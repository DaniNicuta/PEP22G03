class Product:

    def __init__(self):
        self.cathegory = input(' Introduceti numele categoriei ')
        self.name = input(' Introduceti tipul produsului ')
        self.price = input(' Introduceti pretul  ')
        self.stock = input(' Introduceti stocul  ')

    def __repr__(self):
        return 10 * ' = ' + '\n' + 7*' '+ f'Categoria : {self.cathegory}' + '\n'  + 10 * ' = ' + '\n' + 7*' '+ f'Nume produs : {self.name}' + '\n' + 10 * ' = ' + '\n' + 7*' '+ f'Pret : {self.price}' + '\n'  + 10 * ' = ' + '\n' + 7*' '+ f'Stoc : {self.stock}' + '\n' + 10 * ' = '


if __name__ == '__main__':
    camasi = Product()
    print(camasi)
