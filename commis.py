import threading
from abc import ABC, abstractmethod


class Commis(threading.Thread, ABC):
    def __init__(self, nom):
        threading.Thread.__init__(self)
        self.nom = nom

    @abstractmethod
    def run(self):
        pass