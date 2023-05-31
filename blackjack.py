import random

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♣', '♦', '♥']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def get_card_value(card):
    rank = card[0]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)

def calculate_hand_value(hand):
    value = sum(get_card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value

def deal_card(deck, hand):
    card = deck.pop()
    hand.append(card)

def display_hand(hand, title):
    print(f'{title}: ', end='')
    for card in hand:
        print(f'{card[0]}{card[1]}', end=' ')
    print()

def play_blackjack():
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Deal initial cards
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)

    # Display initial hands
    display_hand(player_hand, 'Player Hand')
    display_hand(dealer_hand, 'Dealer Hand (one card hidden)')

    # Player's turn
    while True:
        action = input('Do you want to hit or stand? ').lower()
        if action == 'hit':
            deal_card(deck, player_hand)
            display_hand(player_hand, 'Player Hand')
            if calculate_hand_value(player_hand) > 21:
                print('Player busts! Dealer wins.')
                return
        elif action == 'stand':
            break

    # Dealer's turn
    display_hand(dealer_hand, 'Dealer Hand')
    while calculate_hand_value(dealer_hand) < 17:
        deal_card(deck, dealer_hand)
        display_hand(dealer_hand, 'Dealer Hand')

    # Determine the winner
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    if player_value > 21:
        print('Player busts! Dealer wins.')
    elif dealer_value > 21:
        print('Dealer busts! Player wins.')
    elif player_value > dealer_value:
        print('Player wins.')
    elif player_value < dealer_value:
        print('Dealer wins.')
    else:
        print('It\'s a tie.')

play_blackjack()