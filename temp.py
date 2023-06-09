# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#lesson start
#import section
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#kod bölümü
veriler = pd.read_csv("veriler.csv")

print(veriler)

boykilo = veriler[['boy','kilo']]
print(boykilo)

