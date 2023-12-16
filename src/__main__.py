from node import Node


def main():
    """
    The entry point of the program.

    :return:
    """
    n = Node(parent=None,
             puzzle=[
                 [0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8]
             ])

    print(str(n))


main()
