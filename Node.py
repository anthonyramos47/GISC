import numpy as np 

class node:

    def __init__(self, cnx):
        """Constructor"""
        self.cnx = cnx # Lista de vecinos
        

    def __str__(self):
        return "Conexiones: {}".format(self.cnx)


    