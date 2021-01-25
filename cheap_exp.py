"""
DESCRIPTION:
Bot that tries to play suboptimal in phase 1 to spend the best cards in phase 2.
Phase1; bot will always play the cheapest card possible. 
Also, it won't do marriages.
Phase2; it will play the most expensive card available
and also marriages.
"""

# Import the API objects
from api import State

class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        # type: (State) -> tuple[int, int]
        """
		Function that gets called every turn. This is where to implement the strategies.
		Be sure to make a legal move. Illegal moves, like giving an index of a card you
		don't own or proposing an illegal mariage, will lose you the game.
		TODO: add some more explanation
		:param State state: An object representing the gamestate. This includes a link to
			the states of all the cards, the trick and the points.
		:return: A tuple of integers or a tuple of an integer and None,
			indicating a move; the first indicates the card played in the trick, the second a
			potential spouse.
		"""

        # All legal moves
        moves = state.moves()
        chosen_move = moves[0]

        # play cheapest card in phase 1
        if state.get_phase() == 1:
            # remove marriage in phase 1
            for move in moves:
                if move[1] == None:
                    moves.remove(move)

            # Get move with lowest rank available, of any suit
            for index, move in enumerate(moves):
                if move[0] is not None and move[0] % 5 >= chosen_move[0] % 5:
                    chosen_move = move

        # play most expensive card in phase 2
        if state.get_phase() == 2:
            # Get move with highest rank available, of any suit
            for index, move in enumerate(moves):
                if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                    chosen_move = move

        return chosen_move
