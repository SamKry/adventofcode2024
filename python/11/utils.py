
class int2Array:
    def to2DArray(filename, sepator = None):
        """
        Returns:
            e.g.
            [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        """
        if sepator == None:
            with open(filename) as f:
                return [[int(x) for x in line.strip()] for line in f]
        else:
            with open(filename) as f:
                return [[int(x) for x in line.strip().split(sepator)] for line in f]


    def toArray(filename):
        """
        Returns:
            e.g.
            [[123],
            [456],
            [789]]
        """
        with open(filename) as f:
            return [int(x) for x in f]
        
    def  toOneLineArray(filename, sepator = None):
        """
        Returns:
            e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        if sepator == None:
            with open(filename) as f:
                arr = []
                for line in f:
                    for x in line.strip():
                        arr.append(int(x))
                return arr
        else:
            with open(filename) as f:
                arr = []
                for line in f:
                    for x in line.strip().split(sepator):
                        arr.append(int(x))
                return arr

class char2Array:
    def to2DArray(filename, sepator = None):
        """
        Returns:
            e.g.
            [['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']]
        """
        if sepator == None:
            with open(filename) as f:
                return [[x for x in line.strip()] for line in f]
        else:
            with open(filename) as f:
                return [[x for x in line.strip().split(sepator)] for line in f]

    def toArray(filename):
        """
        Returns:
            e.g.
            ['abc',
            'def',
            'ghi']
        """
        with open(filename) as f:
            return [x.strip() for x in f]
        
    def toOneLineArray(filename):
        """
        Returns:
            e.g. ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        """
        with open(filename) as f:
            arr = []
            for line in f:
                for x in line.strip():
                    arr.append(x)
            return arr