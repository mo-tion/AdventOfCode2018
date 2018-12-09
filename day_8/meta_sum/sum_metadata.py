from node import Node

with open("license.txt", "r") as input_file:
    license_numbers = map(lambda x: int(x), input_file.readlines()[0].split (" "))

node_num = 0

def create_node(start_index):
    # read header
    num_children = license_numbers[start_index]
    num_meta = license_numbers[start_index+1]

    new_node = Node(num_meta, num_children)
    end_index = start_index+2

    for i in range(num_children):
        end_index, new_child = create_node(end_index)
        new_node.add_child(new_child)

    for i in range(num_meta):
        new_node.add_meta(license_numbers[end_index])
        end_index += 1

    return (end_index, new_node)

_, root_node = create_node(0)

print(root_node.sum_meta())