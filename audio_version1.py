# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:13:56 2019

@author: profe
"""
import matplotlib.pyplot as plt
import numpy as np
import wave, os , glob
import pickle

zero=[]
frames=[]
zero1=[]

path= 'C:\\Emotional_recognition\\Actor_01'

filename= os.listdir(path)
#os.makedirs('C:\\Emotional_recognition\\Actor_01_new', exist_ok=True)


for filename in glob.glob(os.path.join(path,'*.wav')):
    

       wave_file=wave.open(filename,'rb')
       
       #dump information to that file 
       
       data=pickle.load(wave_file)
       
       params=wave_file.getparams()

       zero.append(params)
       frames.append(wave_file.readframes(100000))
       
     #open a file, where you want to store the data  
       files= wave.open('C:\\Emotional_recognition\\Actor_01_new','wb')
       
       #dump information to that file
       pickle.dump(zero,frames,files)
     
      #op.setparams(zero)
       #op.writeframes(frames)
       
       files.close()
    
       wave_file.close()

       
   
        
  