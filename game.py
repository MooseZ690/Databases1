import tkinter as tk
import random

# Card values
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}
SUITS = ['♠', '♥', '♦', '♣']
RANKS = list(CARD_VALUES.keys())

def create_deck():
    return [f"{rank}{suit}" for rank in RANKS for suit in SUITS]

def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        score += CARD_VALUES[rank]
        if rank == 'A':
            aces += 1
    # Adjust for Aces if over 21
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        
        # GUI Elements
        self.player_label = tk.Label(root, text="Your Hand: ", font=("Helvetica", 16))
        self.player_label.pack()

        self.dealer_label = tk.Label(root, text="Dealer's Hand: ", font=("Helvetica", 16))
        self.dealer_label.pack()

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack()

        self.hit_button = tk.Button(root, text="Hit", command=self.hit)
        self.hit_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stand_button = tk.Button(root, text="Stand", command=self.stand)
        self.stand_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart)
        self.restart_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.restart()

    def restart(self):
        self.deck = create_deck()
        random.shuffle(self.deck)
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.result_label.config(text="")
        self.update_display()

    def update_display(self, show_dealer=False):
        player_text = "Your Hand: " + ' '.join(self.player_hand) + f" (Score: {calculate_score(self.player_hand)})"
        if show_dealer:
            dealer_text = "Dealer's Hand: " + ' '.join(self.dealer_hand) + f" (Score: {calculate_score(self.dealer_hand)})"
        else:
            dealer_text = "Dealer's Hand: " + self.dealer_hand[0] + " ??"
        self.player_label.config(text=player_text)
        self.dealer_label.config(text=dealer_text)

    def hit(self):
        self.player_hand.append(self.deck.pop())
        score = calculate_score(self.player_hand)
        self.update_display()
        if score > 21:
            self.end_game("You bust! Dealer wins.")

    def stand(self):
        while calculate_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())
        self.update_display(show_dealer=True)
        self.evaluate_winner()

    def evaluate_winner(self):
        player_score = calculate_score(self.player_hand)
        dealer_score = calculate_score(self.dealer_hand)

        if dealer_score > 21:
            self.end_game("Dealer busts! You win!")
        elif player_score > dealer_score:
            self.end_game("You win!")
        elif player_score < dealer_score:
            self.end_game("Dealer wins.")
        else:
            self.end_game("It's a tie.")

    def end_game(self, result):
        self.result_label.config(text=result)
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)

        # Re-enable buttons after delay
        self.root.after(3000, lambda: [
            self.hit_button.config(state=tk.NORMAL),
            self.stand_button.config(state=tk.NORMAL)
        ])

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()
