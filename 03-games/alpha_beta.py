import numpy as np

def is_game_over(node):
    winning_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for indexes in winning_indexes:
        hit_count = 0
        chosen_symbol = node[indexes[0]]

        for index in indexes:
            if node[index] is not None and node[index] == chosen_symbol:
                hit_count = hit_count + 1

        if hit_count == 3:
            return True, chosen_symbol

    if node.count(None) == 0:
        return True, None

    return False, None

def generate_children(node, chosen_symbol): # TODO: Create a function to generate the children states for minimax evaluation
    options=[i for i in range(0,9) if node[i]==None]
    children=[]
    for index,option in enumerate(options):
        children.append(node.copy())
        children[index][option]=chosen_symbol
    return children

def alternate_symbol(symbol):
    return 'o' if symbol == 'x' else 'x'

def mini_max_ab(node, is_maximizing_player_turn, chosen_symbol,alpha,beta): # TODO: Modify this minimax in order to turn it into an alpha-beta pruning version with depth cutting
    game_result = is_game_over(node)

    if game_result[0]:
        if game_result[1] is None:
            return 0, node

        return (-1, node) if is_maximizing_player_turn else (1, node)

    children = generate_children(node, chosen_symbol)
    if is_maximizing_player_turn:
        max_eval=-np.inf
        max_node=None
        for child in children:
            eval,node=mini_max_ab(child, False, alternate_symbol(chosen_symbol),alpha,beta)
            if eval>max_eval:
                max_eval=eval
                max_node=child
            alpha=max(alpha,eval)
            if beta<=alpha:
                break
        return max_eval,max_node
    else:
        min_eval=np.inf
        min_node=None
        for child in children:
            eval,node=mini_max_ab(child, True, alternate_symbol(chosen_symbol),alpha,beta)
            if eval<min_eval:
                min_eval=eval
                min_node=child
            beta=min(beta,eval)
            if beta<=alpha:
                break
        return min_eval,min_node


    # children_results = list(map(
    #     lambda child: [
    #         mini_max(child, not is_maximizing_player_turn, alternate_symbol(chosen_symbol))[0],
    #         child
    #     ],
    #     children
    # ))

    # return max(children_results, key=str) if is_maximizing_player_turn else min(children_results, key=str)

def mini_max(node, is_maximizing_player_turn, chosen_symbol):
    game_result = is_game_over(node)

    if game_result[0]:
        if game_result[1] is None:
            return 0, node

        return (-1, node) if is_maximizing_player_turn else (1, node)

    children = generate_children(node, chosen_symbol)
    children_results = list(map(
        lambda child: [
            mini_max(child, not is_maximizing_player_turn, alternate_symbol(chosen_symbol))[0],
            child
        ],
        children
    ))
    return max(children_results, key=str) if is_maximizing_player_turn else min(children_results, key=str)