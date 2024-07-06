from classes import Piece


def genBoardFromFEN(FEN):
    pieceTypes = {
        'r': "Rook",
        'n': "Knight",
        'b': "Bishop",
        'q': "Queen",
        'k': "King",
        'p': "Pawn"
    }
    
    board = []
    file, row = 0, 0

    for piece in FEN:
        if piece == '/':
            row += 1
            file = 0
            continue
        elif piece.isnumeric():
            for i in range(int(piece)):
                board.append(None)
                file += 1
            continue
        color = "WHITE" if piece.isupper() else "BLACK"
        type = pieceTypes[piece.lower()]

        board.append(Piece(color=color, type=type, row=row, file=file))
        file += 1
 
    return board



