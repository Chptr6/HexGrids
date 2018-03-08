import numpy as np
import collections


class HexUnit(object):
    def __init__(self, position):
        self.position = np.array(position)
        self.update_position()

    def update_position(self):
        lowest = self.position.min()
        self.position -= np.array([lowest, lowest, lowest])

    def standardize(self, vector):
        vector = np.array(vector)
        v_min = vector.min()
        vector -= np.array([v_min, v_min, v_min])
        return vector

    def move(self, vector):
        self.position += np.array(vector)
        self.update_position()

    def find_path_to(self, target):
        target = np.array(target)
        target = self.standardize(target)
        path = target - self.position

        def short_path(dt_displace):
            shortest_path = None
            length = None
            for i in dt_displace:
                choice_path = dt_displace-np.array([i, i, i])
                temp_length = sum(np.absolute(choice_path))
                if length is None or temp_length <= length:
                    length = temp_length
                    shortest_path = choice_path
            return shortest_path

        path = short_path(path)
        return path

    def calculate_path_length(self, target):
        path = self.find_path_to(target)
        return sum(np.absolute(path))

    def test_path(self, path):
        print("Least Distant Analysis")
        print("calc:\t", path, self.calculate_path_length(path))
        for i in range(-5, 5):
            print("+", i, "\t", path+np.array([i, i, i]),
                  sum(np.absolute(path+np.array([i, i, i]))))


ako = HexUnit([0, 0, 0])
path_target = [0, 0, -1]
ako.update_position()
print("Position:\t", ako.position)
print("Target:\t\t", ako.standardize(path_target))
print("Path: \t\t", ako.find_path_to(path_target))
print()
print(ako.test_path(ako.find_path_to(path_target)))
