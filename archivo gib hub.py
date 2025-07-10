#productos= marca, pantalla, ram, disco, GB de DD, procesador, video.

productos= {'8475HD':['hp', '15.6', '8GB', 'DD', '1T', 'intel core i5', 'nvidia GTX1050'],
            '2175HD':['lenovo', '14', '4GB', 'SSD','512GB', 'intel core i5','nvidia GTX1050'],
            'JjFHD': ['azus', '14', '16GB', 'SSD', '256GB', 'intel core i7', 'nvidia rtx2080ti'],
            'fgdxFHD': ['HP', '15.6', '8GB', 'DD', '1T', 'intel core i3', 'integrada'],
            'GF75HD': ['asus', '15.6', '8GB', 'DD', '1T', 'intel core i7', 'nvidia gtx1050'],
            '123fhd' : ['lenovo', '14', '6GB', 'DD', '1T', 'amd ryzen 5', 'integrada'],
            '342fhd': ['lenovo', '15.6', '8GB', 'DD', '1T', 'amd ryzen 7', 'nvidia gtx1050'],
            'UWU131HD': ['dell', '15.6', '8gb', 'DD', '1T', 'amd ryzen 3', 'nvidia gtx1050'],
}

#stock de productos: modelo > [precio, stock]
stock = {
    '8475hd': [387990, 10],
    '2175hd': [327990, 4],
    'JjFfhd': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123fhd': [298090, 32],
    '342fhd' : [444990, 7],
    'GF75Hd': [749990, 2],
    'UWU131HD': [349990,1]
}

def mostrar_titulo(texto):
    print("\n"+ "*" * (len(texto) + 4))
    print(f"* {texto} * +")
    print("*" *(len(texto) + 4))
