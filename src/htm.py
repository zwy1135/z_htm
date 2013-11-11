# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:33:43 2013

@author: wy
"""


import numpy as np
import random



###########################################
#常量定义
###########################################
STATES = {
        'inactive':0,
        'active':1
        'predictive':2
        }
CONNECTED_PERM_THR = 0.2
MIN_OVERLAP = 2
INIT_BOOST = 1
INIT_INHIB_RADIUS = 3
DESIRED_LOCAL_ACTIVITY = 2
PERM_INCR = 0.2
PERM_DECR = 0.2
INIT_PERM = 0.3
N_LATERAL_CONNECTIONS = 2   # usually a dozen
PERC_INTERCONNECTED = 0.5   # percentage of cells laterally connected to a cell
ACTIVATION_THR = 2          # no. of valid synapses on a distal dendrite for it to be active
MIN_THR = 1                 # like ACTIVATION_THR, but during temporal pooler learning
N_NEW_SYNAPSES = 2
SHOW_CELL_DDS = True        # whether to show a cell's distal dendrites in reprs





class Cell:
    '''
    细胞类。
    '''
    def __init__(self,cell_idx,layer_idx):
        pass
    
    
class Synapse:
    def __init__(self,):
        pass
    
    
class ProximalDendrite:
    def __init__(self,):
        pass
    
    
class DistalDendrite:
    def __init__(self,):
        pass


class Region:
    '''
    区域类。
    '''
    def __init__(self,layers_num,cells_num,input_num):
        print 'Creating a %d X %d region. '%(layers_num,cells_num)
        self.cells_num = cells_num
        self.layers_num = layers_num
        self.region = np.array(
                        [[Cell(cell_idx,layer_idx)for cell_idx in range(cells_num)]
                        for layer_idx in range(layers_num)])
                            
                            
                            
                            
        input_idxs = set(range(input_num))
        syns_num = input_num / self.cells_num
        for col_idx,column in enumerate(self.columns):
            potential_syn_idxs = random.sample(input_idxs,syns_num)
            input_idxs -= set(potential_syn_idxs)
            pd = ProximalDendrite(col_idx,potential_syn_idxs,self.cells_num,init_boost,min_overlap)
            for cell in column:
                cell.set_prox_dendr(pd)
        
    #############################################################
    #以下是额外的变量定义
    #############################################################
    @property
    def columns(self):
        return self.region.T
    
    @property
    def layers(self):
        return self.region
       
    @property
    def cells(self):
        return self.region.flatten()
        
    @property
    def prox_dendrites(self):
        return [cell.prox_dendrite for cell in self.layers[0]]
        
    @property
    def active_pds(self):
        return [pd for pd in self.prox_dendrites if pd.is_active]
        
    @property
    def sdr(self):
        return [int(pd.is_active)for pd in self.prox_dendrites]
        
    @property
    def overlaps(self):
        return [pd.overlap for pd in self.prox_dendrites]
    ##############################################################
    #额外变量结束
    ##############################################################        
        
        
    