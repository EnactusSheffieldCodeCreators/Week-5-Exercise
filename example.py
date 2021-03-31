###############################################################################
#                                BOARD CLASS                                  #
###############################################################################
class Board:
    def __init__(self, width, height):
        """
            width: width of the board
            height: height of the board
        """
        self.width = width
        self.height = height
        
        # Now create a board representation
        # This can be a:
        # - Nested list
        # - Single list
        # - Anything (get creative!)
    
    def check_winning_pattern(self):
        """ 
            A method that check if 4 pieces are connected 
            This can be used to find the winner
        """
        pass
        
    def drop_piece(self):
        """ Add a piece to the board """
        pass
        
    def __repr__(self):
        """ Return a pretty-printed representation of the board """
        pass
    

###############################################################################
#                                GAME CLASS                                   #
###############################################################################
class Game:
    def __init__(self, player_1, player_2, width, height):
        """
            player_1: player 1
            player_2: player 2
            width: width of the board
            height: height of the board
        """
        self.board = Board(width, height) 
        self.players = [player_1, player_2]
        
    def change_turn(self):
        """ Switch player's turn """
        pass
        
    def play_game(self):
        """ Let the game start """
        pass
        

###############################################################################
#                                PIECE CLASS                                  #
###############################################################################
class Piece:
    pass


###############################################################################
#                                PLAYER CLASS                                 #
###############################################################################
class Player:
    def __init__(self, piece, name):
        """
            piece: piece color
            name: player name
        """
        self.piece = piece
        self.name = name

    def play_move(self):
        """ Player play a move """
        pass
