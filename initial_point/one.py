import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from new.node import Node
from new.helper import *


def draw_line(x):
    # x_coord = []
    # y_coord = []
    # for i in range(0, len(x.child)):
    #     x_coord.append(x.child[0])
    #     y_coord.append(x.child[1])
    # plt.plot(x_coord, y_coord, color='red')
    # plt.scatter(x_coord, y_coord, linewidths=0.01)
    for i in range(0, len(x.child)):
        parent_x = x.pos[0]
        parent_y = x.pos[1]
        child = x.child[i].pos
        child_x = child[0]
        child_y = child[1]
        plt.plot([parent_x, child_x], [parent_y, child_y], color='red')


def generate_map():
    obstacle1 = plt.Rectangle((-6, -5), 6, 1, color='black')
    obstacle2 = plt.Rectangle((4, -4), 1, 13, color='black')
    init_x = plt.Circle((0, 0), radius=0.5)
    goal_x = plt.Circle((8, 8), radius=0.6, color='green')

    plt.gca().add_patch(obstacle1)
    plt.gca().add_patch(obstacle2)
    plt.gca().add_patch(init_x)
    plt.gca().add_patch(goal_x)

    plt.plot([-10, 10], [-10, 10], 'ro', color='white')
    # plt.gca().add_patch(obstacle2)
    plt.axis('scaled')

    # plt.show()


if __name__ == '__main__':
    generate_map()

    x_init = Node(child=None, parent=None, pos=(0, 0), number=0)

    sample_number = 10

    for i in range(0, sample_number):
        # x_near = sample_uniform(x_init.pos)
        x_near = Node(child=None, parent=x_init, pos=sample_uniform(x_init.pos))
        x_init.child.append(x_near)

    distance = 100
    index = 0
    for i in range(0, len(x_init.child)):
        potential_x = x_init.child[i].pos
        if dist_between_points(x_init.pos, potential_x) < distance:
            index = i
            distance = dist_between_points(x_init.pos, potential_x)
    draw_line(x_init)
    plt.show()

    # ====================================================
    # x_init.next = Node(child=None, parent=x_init, pos=x_init.child[index], number=1)
    # x_next = x_init.next
    #
    # for i in range(0, sample_number):
    #     # x_near = sample_uniform(x_init.pos)
    #     x_near = Node(child=None, parent=x_init, pos=sample_uniform(x_init.pos))
    #     x_next.child.append(x_near)
    #
    # distance = 100
    # index = 0
    #
    # for i in range(0, len(x_next.child)):
    #     potential_x = x_next.child[i].pos
    #     if dist_between_points(x_next.pos, potential_x) < distance:
    #         index = i
    #         distance = dist_between_points(x_next.pos, potential_x)
    #
    # draw_line(x_next)
    #
    # plt.show()
