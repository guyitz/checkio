# from pprint import pprint
#
#
# def _test():
#     from doctest import testmod
#     testmod(verbose=True)
#
# from collections import OrderedDict
#
#
# class Point:
#     """ Point class represents and manipulates x,y coords. """
#
#     def __init__(self, x=0, y=0):
#         """ Create a new point at x, y """
#         self.x = x
#         self.y = y
#
#     def wind_rose_pos_dict(self):
#         return OrderedDict({'S': Point(x=self.x + 1, y=self.y), 'E': Point(x=self.x, y=self.y + 1), 'N': Point(x=self.x - 1, y=self.y), 'W': Point(x=self.x, y=self.y - 1)})
#
#
# def possible_routes(maze_map, pos):
#     pos_dict = pos.wind_rose_pos_dict()
#     for key in pos_dict.keys():
#         if maze_map[pos_dict[key].x][pos_dict[key].y] != 0:
#             pos_dict.pop(key)
#     return pos_dict
#
#
# def checkio_h(maze_map, route, pos):
#     if pos.x == 10 and pos.y == 10:
#         return route
#     possible_routes_dict = possible_routes(maze_map, pos)
#     pprint(maze_map)
#     print "==========================================================================================="
#     if possible_routes_dict:
#         for key in possible_routes_dict.keys():
#             maze_map[possible_routes_dict[key].x][possible_routes_dict[key].y] = 2
#             # if possible_routes_dict[key].x == 10 and possible_routes_dict[key].y == 10:
#             #     return route + key
#             # else:
#             checkio_h(maze_map, route + key, possible_routes_dict[key])
#
#
#
# def checkio(maze_map):
#     return checkio_h(maze_map, "", Point(1, 1))
#
#
# print checkio([
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
#     [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


# New solution

def checkio(maze_list):
    dir_list = []
    start_pos = (1, 1)
    if checkio_h(maze_list, start_pos, dir_list):
        return ''.join(dir_list)


def checkio_h(maze_list, cur_pos, direction_list):
    possible_pos = find_possible_pos(maze_list, cur_pos)
    for pos in possible_pos:
        if pos[0] == pos[1] == 10:
            direction_list.append(pos[2])
            # print ''.join(direction_list)
            return True
        else:
            maze_list[pos[0]][pos[1]] = 2
            direction_list.append(pos[2])
            if checkio_h(maze_list, pos, direction_list):
                return True
            else:
                maze_list[pos[0]][pos[1]] = 0
                direction_list.pop()


def find_possible_pos(maze_list, cur_pos):
    x = cur_pos[0]
    y = cur_pos[1]
    possible_pos = []
    if maze_list[x + 1][y] == 0:
        possible_pos.append((x + 1, y, 'S'))
    if maze_list[x - 1][y] == 0:
        possible_pos.append((x - 1, y, 'N'))
    if maze_list[x][y + 1] == 0:
        possible_pos.append((x, y + 1, "E"))
    if maze_list[x][y - 1] == 0:
        possible_pos.append((x, y - 1, "W"))
    return possible_pos


# print checkio([
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
#         [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
#         [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
#         [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
#         [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
#         [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])



# Not working...
# print checkio([
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

# OK
# print checkio([
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


#
# print checkio( [
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#         [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#         [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#         [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#         [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#         [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#         [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#         [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#         [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#         [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


# print checkio([
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#         [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
#         [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
#         [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
#         [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#         [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])



print checkio([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
