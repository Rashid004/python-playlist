import random

SUITS = ["S", "H", "D", "C"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def card_value(rank):
    if rank in ("J", "Q", "K"):
        return 10
    if rank == "A":
        return 11
    return int(rank)

def hand_value(hand):
    total = sum(card_value(r) for r, s in hand)
    aces = sum(1 for r, s in hand if r == "A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def new_deck():
    deck = [(r, s) for s in SUITS for r in RANKS]
    random.shuffle(deck)
    return deck

def show_hand(hand, label, hide_second=False):
    if hide_second:
        cards = f"{hand[0][0]}{hand[0][1]}  ??"
        print(f"{label}: {cards}")
    else:
        cards = "  ".join(f"{r}{s}" for r, s in hand)
        print(f"{label}: {cards}  (value: {hand_value(hand)})")

def play_round(deck, chips):
    bet = 0
    while bet <= 0 or bet > chips:
        try:
            bet = int(input(f"\nChips: {chips}  —  How much to bet? "))
            if bet <= 0 or bet > chips:
                print("Invalid bet.")
        except ValueError:
            print("Enter a number.")

    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

    print()
    show_hand(dealer, "Dealer", hide_second=True)
    show_hand(player, "You   ")

    # Natural blackjack check
    if hand_value(player) == 21:
        print("\n🃏 Blackjack! You win 1.5x!")
        show_hand(dealer, "Dealer")
        return chips + int(bet * 1.5)

    # Player turn
    while hand_value(player) < 21:
        action = input("\n[h]it  [s]tand? ").strip().lower()
        if action == "h":
            player.append(deck.pop())
            show_hand(player, "You   ")
            if hand_value(player) > 21:
                print("Bust! You lose.")
                return chips - bet
        elif action == "s":
            break

    player_val = hand_value(player)

    # Dealer turn
    print()
    show_hand(dealer, "Dealer")
    while hand_value(dealer) < 17:
        dealer.append(deck.pop())
        show_hand(dealer, "Dealer")

    dealer_val = hand_value(dealer)

    # Outcome
    if dealer_val > 21:
        print("🎉 Dealer busts — you win!")
        return chips + bet
    elif player_val > dealer_val:
        print("🎉 You win!")
        return chips + bet
    elif player_val < dealer_val:
        print("😞 Dealer wins.")
        return chips - bet
    else:
        print("🤝 Push — tie.")
        return chips

def main():
    print("=== BLACKJACK ===")
    print("Beat the dealer. Dealer stands on 17.")
    chips = 100
    deck = new_deck()

    while chips > 0:
        if len(deck) < 10:
            deck = new_deck()
            print("\n--- Deck reshuffled ---")

        chips = play_round(deck, chips)
        print(f"\nChips: {chips}")

        if chips <= 0:
            print("\nBroke. Game over.")
            break

        again = input("\nPlay again? [y/n] ").strip().lower()
        if again != "y":
            print(f"\nCashing out with {chips} chips. GG!")
            break

if __name__ == "__main__":
    main()
