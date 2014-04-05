#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, csv

class Data():

    def __init__(self, countries=['br','pt'], all=False):
    
        self.__data__ = {
            'br':{
                'name':'Brasil',
                'matrix':None,
                'uids':None
            },
            'pt':{
                'name':'Portugal',
                'matrix':None,
                'uids':None
            }
        }

        for country in countries:
            self.set_matrix(country)
            self.set_uids(country)

    def read_data(self, country='br'):
        """Returns CSV's data as matrix (list of lists)"""
        ret = []
        filename = 'csv/userstats-%s.csv' % (country)
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for row in reader:
                ret.append(row)
        ret.pop(0)
        return ret

    def set_matrix(self, country='br'):
        self.__data__[country]['matrix'] = self.read_data(country)

    def uids(self, data):
        ret = set()
        for line in data:
            ret.add(line[0])
        return ret

    def set_uids(self, country='br'):
        data = self.__data__[country]['matrix']
        self.__data__[country]['uids'] = self.uids(data)
    
    def users_in(self, countries):  # TODO: () → all ?
        ret = set()
        for country in countries:
            ret.update(self.__data__[country]['uids'])
        return ret


#countries = ['br','pt']

unipt = Data()

br = unipt.users_in(['br'])
pt = unipt.users_in(['pt'])
p2 = unipt.users_in(['br','pt'])

print 'br      = %s' % ( len(br)           )
print 'pt      = %s' % ( len(pt)           )
print 'br + pt = %s' % ( len(br) + len(pt) )
print 'br ∪ pt = %s' % ( len(p2)           )

# TODO: command-line interpreter
# TODO: this report bellow
"""
br      = 5837 usuários mapearam algo no Brasil
pt      = 4127 usuários mapearam algo em Portugal
br + pt = 9964 é a soma aritmética dos valores acima
br ∪ pt = 9718 usuários mapearam algo no Brasil ou em Portugal
br ∩ pt =  246 usuários mapearam algo no Brasil e em Portugal
"""
