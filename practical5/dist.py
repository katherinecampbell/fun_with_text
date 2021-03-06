'''
Created on Oct 20, 2017

@author: Katherine
'''
import math
from gensim import corpora
from collections import Counter
from scipy.spatial.distance import euclidean, cosine, cdist 
import scipy


def load_docs():
    print("Loading docs...")
    doc1=('d1', 'Advanced Grammar for new English as a Foreign Language Teachers')
    doc2=('d2', 'Learning Teaching: The Essential Guide to Foreign Language Teaching')
    doc3=('d3', 'English Language Teaching Today: Linking Academic Theory and Practice')
    
 
load_docs()
e_dist_1_2 = cdist('d1', 'd2', 'euclidean', p=None, V = None, VI = None, w= None)
e_dist_1_3 = cdist('d1', 'd2', 'euclidean', p=None, V = None, VI = None, w= None)
e_dist_2_3 = cdist('d2', 'd3', 'euclidean', p=None, V = None, VI = None, w= None)
print(e_dist_1_2,e_dist_1_3, e_dist_2_3  )