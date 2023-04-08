#!/usr/bin/env python
# coding: utf-8

#from rdkit import Chem
#from rdkit.Chem import AllChem
from gridData import Grid
import os,sys,string,argparse
from optparse import OptionParser

parser = argparse.ArgumentParser(description="Retrive valute from dx grid.\n")
parser.add_argument('dx',metavar='<dx GRID file>',help="dx format grid file.")
parser.add_argument('x',metavar='<x>',help="x  coordination")
parser.add_argument('y',metavar='<y>',help="y  coordination")
parser.add_argument('z',metavar='<z>',help="z  coordination")
args = parser.parse_args()
grid = args.dx
x = float(args.x)
y = float(args.y)
z = float(args.z)

if not os.path.exists(grid):
   #message = "Sorry, cannot find the "%s" file."
   print("Sorry, cannot find the %s file" % grid)
   sys.exit()

g = Grid(grid)

a=[]
b=[]
c=[]
a.append(x)
b.append(y)
c.append(z)

value = g.interpolated(a,b,c)
print(x,y,z,value[0])
