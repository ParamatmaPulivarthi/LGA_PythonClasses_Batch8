# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 20:57:56 2025

@author: hp
"""

import param_maths
import param_stats
import param_cs



# subject="maths"
# category="add"
# a=10
# b=20


# subject="stats"
# category="min"
# a=10
# b=20

# subject="cs"
# category="basic"

def param_tutuion(subject,category,a,b):
    if subject=="maths":
        print(" maths is available")
        if category=="add":
            print(" addition is available")
            print("the user given numbers",a,b)
            output=param_maths.param_addition(a,b)
            print(" the addition of two values is",output)
    elif subject=="stats"        :
        print(" stats is available")
        if category=="min":
            print("min is avaialble")
            print(" the user given number",a,b)
            ouptut=param_stats.param_minimum(a,b)
            print(" the min value from given number is ", ouptut)
    elif subject=="cs":
        print(" computer science is available")
        if category=="basic":
            print("basic is avaialble")
            output=param_cs.param_csbasic()
            print(" the basic details are ",output)

param_tutuion('maths',"add",10,20)    
param_tutuion('stats',"min",10,20)    
                