
# poniższy import jest tylko do debugowania.
#import file_handling


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """

    # nie musi wyświetlać raportu od tego są funkcję display.
    # genre to gatunek muzyczny
    albums_to_return = []
    for iter in range(0 , len(albums)):
        if albums[iter][3] == genre:
            albums_to_return.append(albums[iter])

    return albums_to_return

#genre = "rock"
#print(get_albums_by_genre(file_handling.import_data( ), genre))


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """

    # longest_album zawiera album oraz jego długość w sekundach
    longest_album = [[],0]

    for i in range(0 , len(albums)):
        time = albums[i][4]
        time = time.split(":")
        #print(time)
        seconds = 0
        if len(time) == 2:
            seconds = int(time[0])*60 + int(time[1])
            #print(seconds)
            if seconds > int(longest_album[1]):
                longest_album[0] = albums[i] 
                longest_album[1] = seconds
    
    return longest_album[0]

#print(get_longest_album(file_handling.import_data( )))


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """

    sum_seconds = 0
    for iterate in range(0,len(albums)):
        time = albums[iterate][4].split(":")
        seconds = int(time[0])*60 + int(time[1])
        sum_seconds += seconds
    to_return = round(float(sum_seconds / 60),2)
    
    return str(to_return)

#print(get_total_albums_length(file_handling.import_data( )))

