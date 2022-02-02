# def run():
#     for contador in range(0,1000):
#         if contador % 2 != 0:
#             continue
#         print(contador)

# if __name__ == '__main__':
#     run()


# def run():
#     for i in range(100):
#         print(i)
#         if i == 8:
#             break


# if __name__ == '__main__':
#     run()


def run():
    texto = input ('Ingresa un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()
