class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def turn_point(self):
        old_x = self.x
        self.x = self.y
        self.y = 3 - old_x


def extract_points(points_list):
    return [Point(x_point, y_point) for x_point, points_str in enumerate(points_list) for y_point, char in
            enumerate(points_str) if char == 'X']


def _test():
    from doctest import testmod
    testmod(verbose=True)


def recall_password(pos_tup, chars_tup):
    """

    >>> recall_password(('X...', '..X.', 'X..X', '....'), ('itdf', 'gdce', 'aton', 'qrdi'))
    'icantforgetiddqd'

    >>> recall_password(('....', 'X..X', '.X..', '...X'), ('xhwc', 'rsqx', 'xqzz', 'fyzr'))
    'rxqrwsfzxqxzhczy'

    :param pos_tup:
    :param chars_tup:
    :return:
    """
    points_list = extract_points(pos_tup)
    output = ""
    for turn in range(4):
        for point in sorted(points_list, key=lambda point_att: (point_att.x, point_att.y)):
            output += chars_tup[point.x][point.y]
            point.turn_point()
    return output
