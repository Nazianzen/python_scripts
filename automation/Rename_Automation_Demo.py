# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 13:23:21 2019

@author: GIDEON
"""

import os

os.chdir('B:\Videos\Tutorial videos\Python\Django\Django_Blog')

for i in range(12, 15):
    f = os.listdir()[i]
    f_name, f_ext = os.path.splitext(f)

    f_empty, f_title = f_name.split('Python Django Tutorial- ')

    new_name = '{}-{}{}'.format((i + 1), f_title, f_ext)

    os.rename(f, new_name)


# for f in os.listdir():
#    f_name, f_ext = os.path.splitext(f)
#
#    if f_name.__contains__('Python'):
#        f_names = [f_name]
#        print(f_names)
#
#    f_course, f_title = f_name.split('Part')
#    f_num, title = f_title.split(' - ')
#
#    f_course = f_course.strip()
#    f_title = f_title.strip()
#    f_num = f_num.strip().zfill(2)
#
#    new_name = '{}-{}{}'.format(f_num, title, f_ext)
#
#    os.rename(f, new_name)
#
