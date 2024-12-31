#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:57:11 2024

@author: ugurburak
"""

import numpy as np
import matplotlib.pyplot as plt

def heceleme(s):
    
    n=len(s)
    kelime = ""
    s1 = ""
    hece = ""
    sesli = False
    
    for i in range (n-1,-1,-1):
        
        if s[i] in ["a","e","ı","i","o","ö","u","ü","â"]:
            if sesli == True:
                kelime = hece +" - "+kelime
                hece = s[i]
            else:
                sesli = True
                hece =s[i]+hece
        else:
            if sesli == True:
                hece = s[i]+hece
                kelime = hece+" - "+kelime
                hece =""
                sesli = False
            else:
                hece = s[i] + hece
                
    kelime = hece+" - "+kelime
    return kelime

    cümle = ""
    kelime = ""
    
    
    for i in range(len(s)):
        if s[i] not in [" ", ".",",","!",":",";"]:
            kelime += s[i]
        else:
            cümle += ""+heceleme(kelime)
            kelime = ""
    
s = "Yapay zekâ, idealleştirilmiş bir perspektife göre, insan zekâsının özgü yüksek bilişsel fonksiyonları veya otonom davranışları sergileyen bir yapay işletim sistemidir. Bu sistem, algılama, öğrenme, çoğul kavramları bağlama, düşünme, fikir yürütme (belirtme), sorun çözme, iletişim kurma ve karar verme gibi yeteneklere sahip olmalıdır. Ayrıca, bu yapay zekâ sistemi düşüncelerinden tepkiler üretebilmeli (eyleyici yapay zekâ) ve bu tepkileri fiziksel olarak dışa vurabilmelidir."
hecelenmiş = heceleme(s)
print(s,"\n",hecelenmiş)                        
                        
                        
                        
                        
                        
                        