# -*- coding: utf-8 -*-
def trim(s):
        print(s[:1])
        while s[:1] ==' ':
                s = s[1:]
        while s[-1:] ==' ':
                s = s[:-1]
        return s
# print('123',trim('    Hello    '),'123123')
trim('    Hello    ')