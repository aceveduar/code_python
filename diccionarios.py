def run():
    poblacion_paises = {
        'Argentina': 45845,
        'Blasi': 45862,
        'Mexico': 32652,
    }



    for pais, poblacion in poblacion_paises.items():
        print(pais + 'Tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()
