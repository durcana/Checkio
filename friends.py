class Friends:
    def __init__(self, connections):
        self.connections = connections
        connect = dict()
        for i in connections:
            i = list(i)
            print connect.setdefault(i[0], []).append(i[1])
            print connect.setdefault(i[1], []).append(i[0])

    def add(self, connection):
        #Making connection into a list because otherwise checkio says index doesn't work.
        connection = list(connection)
        if connection[0] in connect.keys() or connection[1] in connect.keys():
            return False
        else:
            robot1, robot2 = connection.split("-")
            connect.setdefault(robot1, []).append(robot2)
            connect.setdefault(robot2, []).append(robot1)

    def remove(self, connection):
        connection = list(connection)
        if connection[0] in connect[connection[1]]:
            connect.setdefault(connection[1], []).remove(connection[0])
        elif connection[1] in connect[connection[0]]:
            connect.setdefault(connection[0], []).remove(connection[1])
        else:
            return False

    def names(self):
        return connect.keys()

    def connected(self, name):
        return connect[name]
