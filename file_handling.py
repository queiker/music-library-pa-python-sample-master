def import_data(filename='albums_data.txt'):
    """
    Import data from a file to a list. Expected returned data format:
        ["David Bowie", "Low", "1977", "rock", "38:26"],
        ["Britney Spears", "Baby One More Time", "1999", "pop", "42:20"],
        ...]

    :param str filename: optional, name of the file to be imported

    :returns: list of lists representing albums' data
    :rtype: list

    with open(filename,"r") as f:

        read_data = f.read()
    
    read_data = read_data.split("\n")
    #print(read_data)

    for i in range(0, len(read_data)):
        read_data[i].split(",")

    #print(read_data)
    #poniższy fragment kodu dzieli utwory na pojedyńcze treści z fragmentów:
    #'Pink Floyd,The Dark Side Of The Moon,1973,progressive rock,43:00' robi :
    #"Britney Spears", "Baby One More Time", "1999", "pop", "42:20"

    for i in range(0,len(read_data)):
        line1 = str(read_data[i])
        line1 = line1.split(',')
        read_data[i] = line1
        # if len(read_data[i]) == 5:
        #     read_data[i][0] = str(read_data[i][0])
        #     read_data[i][1] = str(read_data[i][1])
        #     read_data[i][2] = int(read_data[i][2])
        #     read_data[i][3] = str(read_data[i][3])
        #     read_data[i][4] = str(read_data[i][4])
    
    
    #print(read_data)

    #poniżej jest kod kasujący puste linie które w tabeli były by jako ''
    lines_do_delete = []
    for i in range(0,len(read_data)):

        if read_data[i] == ['']:

            lines_do_delete.append(i)

    for i in range(len(lines_do_delete), 0, -1):
        read_data.pop(lines_do_delete[i-1])

    return read_data
        


#Poniżej kod testujący funkcję import_data
#print(import_data('albums_data.txt') )

#import_data('albums_data.txt')


def export_data(albums, filename='albums_data.txt', mode='a'):
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list albums: albums' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """


    if mode == 'a':
        existing_albums = import_data(filename)
        
        for iterate in range(0, len(albums)):
            existing_albums.append(albums[iterate])
        albums = existing_albums

        with open(filename, 'w') as line:
            for i in range(0,len(albums)):
                if len(albums[i]) == 5:
                    line.write(",".join(albums[i]) + "\n")

    elif mode == 'w':
        with open(filename, 'w') as line:
            for i in range(0,len(albums)):
                if len(albums[i]) == 5:
                    line.write(",".join(albums[i]) + "\n")
                    
    else:
        raise ValueError
    

    #print(albums)


#print(export_data([["YYYYYYYYYYYYYYYYYYYYYYYY", "Baby One More Time", "1999", "pop", "42:20"],["XXXXXXXXXXXXXXXXX", "Low", "1977", "rock", "38:26"] ], filename='albums_data.txt', mode='a') )

#print(export_data([["HIHI HEY HEY", "Baby One More Time", "1999", "pop", "42:20"]], filename='albums_data.txt', mode='a') )

