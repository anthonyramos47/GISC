import numpy as np 

class node:

    def __init__(self, *argv):
        """Constructor"""
        self.cnx = argv[0] # Lista de vecinos
        

    def __str__(self):
        return "Conexiones: {}".format(self.cnx)


    