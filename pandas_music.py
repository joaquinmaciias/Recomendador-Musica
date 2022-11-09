import pandas as pd
import re
import os


def extract(csv_name):

    df = pd.read_csv(csv_name + ".csv")  # Si lees un csv no hace falta poner "sep = ","" si estan separados por ","

    return df


def transform(df, opc):

    df_transform = df.loc[:, ['artist', 'song', 'genre', 'energy']]

    list_transform = df_transform.values.tolist()

    # Lista de artista

    list_artist = []

    for artist1 in list_transform:

        repetition = False

        for artist2 in list_artist:

            if artist1[0] == artist2:

                repetition = True

        if not repetition:
            list_artist.append(artist1[0])

    # Lista generos

    list_genre = []

    for genre1 in list_transform:

        genre1[2] = genre1[2].replace(', ', ',')

        genres_songs = re.findall(r'([^,]+)(?:,|$)', genre1[2])

        for genre2 in genres_songs:   # Algunas canciones tienes mas de un genero, por lo que los separamos

            repetition = False

            for genre3 in list_genre:

                if genre2 == genre3:

                    repetition = True

            if not repetition:
                list_genre.append(genre2)

    # Lista de energía

    list_energy = []

    for energy in list_transform:

        list_energy.append(energy[3])

    if opc == 1:

        os.system('cls')

        print('Lista de artista:\n')

        line = ''
        counter = 1

        for artist in list_artist:

            if counter % 8 != 0:
                line += artist + '      |       '
            else:
                line += artist + '      |       '
                line += '\n'
                print(line)
                line = ''

            counter += 1

        print(line)
        print('\n')

        artist_exist = False

        artists_str = ''

        for artist in list_artist:
            artists_str += artist + '   '

        while not artist_exist:

            selec_artist = input('Selecione el artista que deseas escuchar: ')

            if not re.search(selec_artist, artists_str):

                print('El artista seleccionado no existe en la lista.')
                input('Vuelva a seleccionar el artista.')

            else:

                artist_exist = True

        songs = 'Sus canciones son: '

        for artist in list_transform:

            if artist[0] == selec_artist:

                songs += artist[1] + '      |       '

        print(songs)

        input()

        os.system('cls')

    elif opc == 2:

        os.system('cls')

        print('Lista de generos musicales:\n')

        line = ''
        counter = 1

        for genre in list_genre:

            if counter % 6 != 0:
                line += genre + '      |       '
            else:
                line += genre + '      |       '
                line += '\n'
                print(line)
                line = ''

            counter += 1

        print(line)
        print('\n')

        genre_exist = False

        genre_str = ''

        for genre in list_genre:

            genre_str += genre + ' '

        while not genre_exist:

            selec_genre = input('Selecione el genero musical que deseas escuchar: ')

            if not re.search(selec_genre, genre_str):

                print('El genero seleccionado no existe en la lista.')
                input('Vuelva a seleccionar el genero musical.')

            else:

                genre_exist = True

        os.system('cls')

        songs = 'Las canciones de ese genero son: '

        counter = 1

        for genre in list_transform:

            genres_songs = re.findall(r'([^,]+)(?:,|$)', genre[2])

            for genre1 in genres_songs:

                if genre1 == selec_genre:

                    if counter % 6 != 0:

                        songs += genre[1] + '      |       '

                    else:
                        songs += genre[1] + '      |       '
                        songs += '\n'
                        print(songs)
                        songs = ''

                    counter += 1
        print(songs)

        input()

        os.system('cls')

    else:

        os.system('cls')

        print('Rango de nivel de energía de las canciones:\n')

        print('Nivel máximo de energía: ', max(list_energy))
        print('Nivel mínimo de energía: ', min(list_energy))

        error = True

        while error:

            range = input('Selcciona el rango de energía (<<Numbero mínimo>>,<<Número máximo>>): ')
            range = re.findall(r'([^,]+)(?:,|$)', range)

            try:
                error = False
                range[0], range[1] = float(range[0]), float(range[1])

            except:

                error = True
                print('Valor introduccido incorrecto.')

            if range[0] > range[1]:
                error = True
                print('Límite inferior mayor que es superior.')
                input('Vuelve a introducirlo.')

        os.system('cls')

        print('Las canciones en ese rango de energía son: \n')

        line = ''
        counter = 1

        for songs in list_transform:

            song = ''

            if songs[3] >= range[0] and songs[3] <= range[1]:

                song = songs[1]

                if counter % 8 != 0:
                    line += song + '      |       '
                else:
                    line += song + '      |       '
                    line += '\n'
                    print(line)
                    line = ''

                counter += 1

        input(line)
        print('\n')


def menu():

    os.system('cls')

    print("-------------------------------------------")
    print("|                                         |")
    print("|   1. Caciones de un artista             |")
    print("|   2. Genero de música                   |")
    print("|   3. Rango de energía de las canciones  |")
    print("|   4. Salir                              |")
    print("|                                         |")
    print("-------------------------------------------\n")

    opc = input('Seleccione la opción que desees: ')

    os.system('cls')

    return opc


if __name__ == "__main__":

    df_orig = extract("songs_normalize")

    opc = 0

    while opc != '4':

        error = False

        while not error:

            opc = menu()

            if opc == '1' or opc == '2' or opc == '3' or opc == '4':

                error = False

            else:

                error = True

            if opc != '4':

                if not error:

                    opc = int(opc)

                    df_transform = transform(df_orig, opc)

                else:

                    print('El valor introducido no es correcto.\n')
                    input('Vuelva a introducirlo.\n')
                    os.system('cls')
            else:
                error = True
