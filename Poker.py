'''
Description: Simulating a Poker game. The deck is a standard 52 card deck.
Cards are ranked from high to low: Ace, King, ..., 3, 2. There are fours
suits - Spades, Hearts, Clubs, and Diamonds. Suits are of equal value.
Each player is dealt five cards. The player with the highest values hand wins.
Hand ranks:
   1. Royal flush
   2. Straight Flush
   3. Four of a Kind
   4. Full House
   5. Flush
   6. Straight
   7. Three of a Kind
   8. Two Pair
   9. One Pair
   10. High Card
Student's Name: Sayuri Monarrez Yesaki
Student's UT EID: sdm3465
Course Name: CS 313E Elements of Software design
Unique Number: 51335
Date Created: 02/2/2018
Date Last Modified: 02/8/2018
'''

import random

class Card (object):
   RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

   SUITS = ('C', 'D', 'H', 'S')

   def __init__ (self, rank = 12, suit = 'S'):
      if (rank in Card.RANKS):
         self.rank = rank
      else:
         self.rank = 12

      if (suit in Card.SUITS):
         self.suit = suit
      else:
         self.suit = 'S'

   def __str__ (self):
      if (self.rank == 14):
         rank = 'A'
      elif (self.rank == 13):
         rank = 'K'
      elif (self.rank == 12):
         rank = 'Q'
      elif (self.rank == 11):
         rank = 'J'
      else:
         rank = str (self.rank)
      return rank + self.suit

   # para imprimir objetos dentro de una lista
   __repr__ = __str__

   def __eq__ (self, other):
      return (self.rank == other.rank)

   def __ne__ (self, other):
      return (self.rank != other.rank)

   def __lt__ (self, other):
      return (self.rank < other.rank)

   def __le__ (self, other):
      return (self.rank <= other.rank)

   def __gt__ (self, other):
      return (self.rank > other.rank)

   def __ge__ (self, other):
      return (self.rank >= other.rank)

class Deck (object):
   def __init__ (self):
      self.deck = []
      for suit in Card.SUITS:
         for rank in Card.RANKS:
            card = Card (rank, suit)
            self.deck.append (card)

   def shuffle (self):
      random.shuffle (self.deck)

   def deal (self):
      if (len(self.deck) == 0):
         return None
      else:
         return self.deck.pop(0)

class Poker (object):
   HANDS = {
   1 : "Royal Flush",
   2 : "Straight Flush",
   3 : "Four of a Kind",
   4 : "Full House",
   5 : "Flush",
   6 : "Straight",
   7 : "Three of a Kind",
   8 : "Two Pair",
   9 : "One Pair",
   10: "High Card"
   }

   def __init__ (self, num_players):
      self.deck = Deck()
      self.deck.shuffle()
      self.players = []
      numcards_in_hand = 5

      for i in range (num_players):
         hand = []
         for j in range (numcards_in_hand):
            hand.append (self.deck.deal())
         self.players.append (hand)

   def play (self):
      # sort the hands of each player and print
      print()
      for i in range (len(self.players)):
         sortedHand = sorted (self.players[i], reverse = True)
         self.players[i] = sortedHand
         hand = ''
         for card in sortedHand:
            hand = hand + str (card) + ' '
         print ('Player ' + str (i + 1) + " : " + hand)

      self.det_type_hand()
      self.det_winner()

   # determine each type of hand and print
   def det_type_hand (self):
      self.points_hand = []  # create list to store points for each hand
      for i in range(len(self.players)):
         hand = self.players[i]
         total_points = 0
         types_of_hands = [self.is_royal, self.is_straight_flush, self.is_four_kind, self.is_full_house,\
            self.is_flush, self.is_straight, self.is_three_kind, self.is_two_pair, self.is_one_pair,\
            self.is_high_card]
         count = 1
         for is_hand in types_of_hands:
            total_points = is_hand(hand)

            if total_points != 0:
               break
            else:
               count += 1
         self.points_hand.append((Poker.HANDS[count], total_points, i+1))


   def det_winner(self):
      # determine winner and print
      print()
      for i in range(len(self.players)):
         print ('Player ' + str (i + 1) + " : " + self.points_hand[i][0])

      winner_list = sorted (self.points_hand, key = lambda hand_type : hand_type[1], reverse = True)
      tie_count = 0
      print()
      for i in range(1, len(winner_list)):
         if winner_list[i][0] == winner_list[0][0]:
            tie_count += 1
         else:
            break
      if tie_count == 0:
         print ('Player ' + str(winner_list[0][2]) + ' wins')
      else:
         for i in range(tie_count + 1):
            print ('Player ' + str(winner_list[i][2]) + ' ties.')

   # determine if a hand is a royal flush
   def is_royal (self, hand):
      same_suit = True
      for i in range (len(hand) - 1):
         same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

      if (not same_suit): # if (same_suit == False)
         return 0

      rank_order = True
      for i in range (len(hand)):
         rank_order = rank_order and (hand[i].rank == 14 - i)

      if (same_suit and rank_order):
         h = 10
         total_points = self.assign_points (hand, h)
         return total_points
      return 0

   def is_straight_flush (self, hand):
      same_suit = True
      for i in range (len(hand) - 1):
         same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

      if (not same_suit):
         return 0

      rank_order = True
      for i in range(len(hand)-1):
         rank_order = rank_order and (hand[i].rank == hand[i + 1].rank + 1)

      if (same_suit and rank_order):
         h = 9
         total_points = self.assign_points (hand, h)
         return total_points
      return 0

   def is_four_kind (self, hand):
      count = self.eq_cards (hand)
      if count == 3 and ((hand[0].rank != hand[1].rank) or (hand[3].rank != hand[4].rank)):
         h = 8
         total_points = self.pts_four_kind (hand, h)
         return total_points
      else:
         return 0

   def is_full_house (self, hand):
      count = self.eq_cards (hand)
      if count == 3:
         h = 7
         total_points = self.pts_full_house (hand, h)
         return total_points
      else:
         return 0

   def is_flush (self, hand):
      same_suit = True
      for i in range (len(hand) - 1):
         same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

      if (not same_suit): # if (same_suit == False)
         return 0
      else:
         h = 6
         total_points = self.assign_points (hand, h)
         return total_points

   def is_straight (self, hand):
      num_order = True
      for i in range (len(hand) - 1):
         num_order = num_order and (hand[i].rank == hand[i + 1].rank + 1)

      if (not num_order):
         return 0
      else:
         h = 5
         total_points = self.assign_points( hand, h)
         return total_points

   def is_three_kind (self, hand):
      count = self.eq_cards (hand)
      if count == 2 and ((hand[0].rank == hand[1].rank == hand[2].rank) or \
         (hand[1].rank == hand[2].rank == hand[3].rank) or \
         (hand[2].rank == hand[3].rank == hand[4].rank)):
         h = 4
         total_points = self.pts_three_kind(hand, h)
         return total_points
      else:
         return 0

   def is_two_pair (self, hand):
      count = self.eq_cards (hand)
      if count == 2:
         h = 3
         total_points = self.pts_two_pair(hand, h)
         return total_points
      else:
         return 0

   # determine if a hand is one pair
   def is_one_pair (self, hand):
      for i in range (len(hand) - 1):
         if (hand[i].rank == hand[i + 1].rank):
            h = 2
            total_points = self.pts_one_pair(hand, h)
            return total_points
      return 0

   def is_high_card (self, hand):
      h = 1
      total_points = self.assign_points(hand, h)
      return total_points

   def assign_points (self, hand, h):
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      total_points = h * 13 ** 5 + c1 * 13 ** 4 + c2 * 13 ** 3 + c3 * 13 ** 2 + c4 * 13 + c5
      return total_points

   def pts_four_kind (self, hand, h):
      if (hand[0].rank == hand[1].rank):
         total_points = self.assign_points (hand, h)
      else:
         c1 = hand[1]
         c2 = hand[2]
         c3 = hand[3]
         c4 = hand[4]
         c5 = hand[0]
         total_points = self.assign_points([c1, c2, c3, c4, c5], h)
      return total_points

   def pts_full_house (self, hand, h):
      if (hand[0].rank == hand[1].rank == hand[2].rank):
         total_points = self.assign_points (hand, h)
      else:
         c1 = hand[2]
         c2 = hand[3]
         c3 = hand[4]
         c4 = hand[0]
         c5 = hand[1]
         total_points = self.assign_points([c1, c2, c3, c4, c5], h)
      return total_points

   def pts_three_kind (self, hand, h):
      if (hand[0].rank == hand[1].rank == hand[2].rank):
         total_points = self.assign_points (hand, h)
      elif (hand[1].rank == hand[2].rank == hand[3].rank):
         c1 = hand[1]
         c2 = hand[2]
         c3 = hand[3]
         c4 = hand[0]
         c5 = hand[4]
         total_points = self.assign_points([c1, c2, c3, c4, c5], h)
      else: #(hand[2].rank == hand[3].rank == hand[4].rank))
         c1 = hand[2]
         c2 = hand[3]
         c3 = hand[4]
         c4 = hand[0]
         c5 = hand[1]
         total_points = self.assign_points([c1, c2, c3, c4, c5], h)
      return total_points

   def pts_two_pair (self, hand, h):
      if (hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank):
         total_points = self.assign_points (hand, h)
      elif (hand[0].rank == hand[1].rank and hand[3].rank == hand[4].rank):
         c1 = hand[0]
         c2 = hand[1]
         c3 = hand[3]
         c4 = hand[4]
         c5 = hand[2]
         total_points = self.assign_points([c1, c2, c3, c4, c5], h)
      elif (hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank):
         c1 = hand[1]
         c2 = hand[2]
         c3 = hand[3]
         c4 = hand[4]
         c5 = hand[0]
         total_points = self.assign_points([c1, c2, c3, c4, c5], h)
      return total_points

   def pts_one_pair (self, hand, h):
      if (hand[0].rank == hand[1].rank):
         total_points = self.assign_points (hand, h)
      elif (hand[1].rank == hand[2].rank):
         c1 = hand[1]
         c2 = hand[2]
         c3 = hand[0]
         c4 = hand[3]
         c5 = hand[4]
         total_points = self.assign_points([c1, c2, c3, c4, c5], h)
      elif (hand[2].rank == hand[3].rank):
         c1 = hand[2]
         c2 = hand[3]
         c3 = hand[0]
         c4 = hand[1]
         c5 = hand[4]
         total_points = self.assign_points([c1, c2, c3, c4, c5], h)
      elif (hand[3].rank == hand[4].rank):
         c1 = hand[3]
         c2 = hand[4]
         c3 = hand[0]
         c4 = hand[1]
         c5 = hand[2]
         total_points = self.assign_points([c1, c2, c3, c4, c5], h)
      return total_points

   def eq_cards (self, hand):
      count = 0
      for i in range (len(hand) - 1):
         if (hand[i].rank == hand[i+1].rank):
            count += 1
         else:
            continue
      return count

def main():
   # prompt user to enter the number of players
   num_players = int (input ('Enter number of players: '))
   while ((num_players < 2) or (num_players > 6)):
      num_players = int (input ('Enter number of players: '))

   # create the Poker object
   game = Poker (num_players)

   # play the game (poker)
   game.play()

main()
