from itertools import groupby
from collections import UserList


class Database(UserList):

    def __init__(self, L, **kwargs):
        super(Database, self).__init__(L)
        for k, v in kwargs.items():
            setattr(self, k, v)

    # -----------------------------------------------------------------------------
    #    méthodes pour avoir un comportement de liste.
    # -----------------------------------------------------------------------------
    def __getitem__(self, index):
        if isinstance(index, int):
            return super(Database, self).__getitem__(index)
        return Database(super(Database, self).__getitem__(
            index), **{k: v for k, v in self.__dict__.items() if k != "data"})

    def __iter__(self):
        for m in self.data:
            yield m

    def append(self, item):
        self.data.append(item)

    def groupby(self, *args):
        """Cette fonction permet de faire un itérateur en rassemblant les souris
        qui ont les attributs listés dans args égaux

        Args:
            *args: liste d'attributs à matcher entre eux

        Returns:
            iterator: liste de tuples (key, list of objects). Comme pour le
            groupby de pandas
        """
        def keyfunc(x):
            return [getattr(x, attr) for attr in args]
        return groupby(sorted(self.data, key=keyfunc), key=keyfunc)
