#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length == 2 and sum(weights) == limit:
        return (1, 0)




    for weight_ind in range(len(weights)):
        hash_table_insert(ht, weights[weight_ind], weight_ind)

    for weight in weights:
        weight_index = hash_table_retrieve(ht, weight)
        opp_index = hash_table_retrieve(ht, limit - weight)
        if opp_index:
            opp_weight = weights[opp_index]
            a = opp_index if opp_index > weight_index else weight_index
            b = opp_index if opp_index < weight_index else weight_index
            return (a, b)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
