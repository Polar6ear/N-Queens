#                               <--- Knapsack --->
#                           ____________________________

from tabulate import tabulate

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def print_table(selected_items, max_value):
    headers = ["Item", "Weight", "Value"]
    table_data = [(i+1, item.weight, item.value) for i, item in enumerate(selected_items)]
    table_data.append(["Total", "", max_value])

    print("\n Selected Items:")
    print(tabulate(table_data, headers, tablefmt="grid"))

items = [
 #(value, weight)
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]

max_weight = 50



#                               <--- Brute Force --->
#                            ___________________________
'''
    Assume the scenario :
    ___________________________

    [KNAPSACK]: We have a knapsack to carry products for selling.

    It holds up to a certain weight, not enough to carry all products.

    must choose which one to carry.

    Knowing the weight and sales value of each product ---> which one we should chose to get hightest revenue?
'''

from itertools import combinations


def knapsack(items, max_weight):
    n = len(items)
    max_value = 0
    best_combination = []

    #generate all subset of items
    for i in range(1, n + 1):
        for subset in combinations(range(n), i):
            total_weight = sum(items[i].weight for i in subset)
            total_value = sum(items[i].value for i in subset)

            if total_weight <= max_weight and total_value > max_value:
                max_value = total_value
                best_combination = subset

    select_items = [items[i] for i in best_combination]
    return select_items, max_value

selected_items, max_value = knapsack(items, max_weight)
print_table(selected_items, max_value)


#                      <---  Heuristics(Greedy)  --->
#                   ___________________________________
'''
    Assume another situation:
    ______________________________

    [EVIL KNAPSACK]: This time a greedy burglar breaks into a home to steal.
    He decided to use Knapsack to carry the stolen items.
    Which item will he steal? Remember, the less time he spends in that home,
    the less likely he is to get caught.

'''

#Greedy KnapSack Function
def greedy_knapsack(items, max_weight):
    sort_items = sorted(items, key=lambda item: item.ratio, reverse=True)

    bag_weight = 0
    bag_items = []

    for item in sort_items:
        if bag_weight + item.weight <= max_weight:
            bag_weight += item.weight
            bag_items.append(item)

    total_value = sum(item.value for item in bag_items)
    return bag_items, total_value

selected_items, total_value = greedy_knapsack(items, max_weight)

print_table(selected_items, total_value)




