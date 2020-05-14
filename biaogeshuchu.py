# -*- coding: utf-8 -*-

from prettytable import PrettyTable

table = PrettyTable(['Province',' Area(km2)','Pop.(10K)'])
table.add_row(['anhui','139600.00','6461.00'])
table.add_row(['beijing','16410.54','1180.70'])
table.add_row(['chongqing','82400.00','3144.23'])
table.add_row(['shanghai','6340.50','1360.26'])
table.add_row(['zhejiang','101800.00','4894.00'])
print(table)