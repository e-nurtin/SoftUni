# cards_as_list = input().split()
# count_of_shuffles = int(input())
#
#
# for shuffle in range(count_of_shuffles):
#     shuffled_deck = []
#     half_deck = len(cards_as_list) // 2
#     right_half = cards_as_list[half_deck:]
#     left_half = cards_as_list[0:half_deck]
#     for element in range(half_deck):
#         shuffled_deck.append(left_half[element])
#         shuffled_deck.append(right_half[element])
#     cards_as_list = shuffled_deck
#
# print(cards_as_list)
#
initial_deck = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    right_half = initial_deck[len(initial_deck) // 2:]
    initial_deck = initial_deck[:len(initial_deck) // 2]
    index = 1
    for i in range(len(initial_deck)):
        initial_deck.insert(index, right_half[i])
        index += 2
print(initial_deck)
