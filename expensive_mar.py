"""
Description: 
expensive_mar bot will always play the most expensive card
but in phase1, it tries to avoid using marriage cards(king and queen)
This way, there is a higher chance it will perform marriages in phase 2.
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

        # marriage cards (king and queen)
        marriage_cards = []
        non_marriage_cards = []

        # play most expensive card in phase 1
        if state.get_phase() == 1:
            # sort marriage cards and non_marriage cards
            for index, move in enumerate(moves):
                # if card is king or queen
                if move[0] is not None and move[0] % 5 == 2 or move[0] is not None and move[0] % 5 == 3:
                    marriage_cards.append(move)
                else:
                    non_marriage_cards.append(move)

            # play most expensive non marriage card if available
            if len(non_marriage_cards) > 0:
                # Get move with highest rank available, of any suit
                chosen_move = non_marriage_cards[0]
                for index, move in enumerate(non_marriage_cards):
                    if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                        chosen_move = move
            else: # play most expensive card available
                chosen_move = moves[0]
                # Get move with highest rank available, of any suit
                for index, move in enumerate(moves):
                    if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                        chosen_move = move

        # play most expensive card in phase 2. also marriages
        if state.get_phase() == 2:
            chosen_move = moves[0]
            # Get move with highest rank available, of any suit
            for index, move in enumerate(moves):
                if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                    chosen_move = move

        return chosen_move
