"""
The main program should use functions from music_reports and display modules
"""

import file_handling
import display
import music_reports


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """

    albums = file_handling.import_data()
    
    #display.print_album_info(albums[0])

    #display.print_albums_list(albums)
    
    
    #music_reports.get_albums_by_genre()
    #music_reports.get_longest_album()
    #music_reports.get_total_albums_length()

    menu_commands_main = ["Print albums list", "Albums reports","Exit program"]
    menu_commands_reports = ["Get albums by genre","Get longest album","Get total albums length","Return main menue"]

    while True:
        display.print_program_menu( menu_commands_main )
        user_input = int(input("Put number"))
        if user_input == 0:
            display.print_albums_list(albums)
        elif user_input == 1:

            while True:
                display.print_program_menu( menu_commands_reports )
                user_input = int(input(("Put number")))
                if user_input == 0:
                    genre = input("Put genre :")
                    albums_by_genre = music_reports.get_albums_by_genre(albums, genre)
                    display.print_albums_list(albums_by_genre)
                elif user_input == 1:
                    display.print_albums_list([music_reports.get_longest_album(albums)])
                elif user_input == 2:
                    display.print_command_result(music_reports.get_total_albums_length(albums))
                elif user_input == 3:
                    pass


                break
        
        elif user_input == 2:
            break


if __name__ == '__main__':
    main()
