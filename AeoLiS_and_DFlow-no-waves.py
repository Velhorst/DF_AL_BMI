# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 11:28:06 2016

@author: velhorst
"""
#==============================================================================
# Importing necessary stuf
# ============================================================================

# for aeolis
from aeolis.model import AeoLiSRunner
from aeolis.model import AeoLiS

# for dflow
from bmi.wrapper import BMIWrapper
BMIWrapper.known_paths.append(r'C:/vanArjen-Dflow_setup/fm_versions/16Aug/win64/dflowfm') #set path to library
BMIWrapper.known_paths.append(r'C:/vanArjen-Dflow_setup/fm_versions/16Aug/win64/wave/bin')


#==============================================================================
# Loading models and configuration files
#============================================================================

# AeoliS
AL_runner = AeoLiSRunner('aeolis_test.txt')
AL_model = AeoLiS('aeolis_test.txt')

# DFlow
mdu_file = r'C:/vanArjen-Dflow_setup/Zandmotor_FM_Aug2016_run06_BMIwrapper/fm/zm_dfm.mdu' # set path to ini file
DF_wrapper = BMIWrapper(engine="dflowfm", configfile=mdu_file)

#==============================================================================
# Initializing
#============================================================================

AL_model.initialize()
DF_wrapper.initialize()

#==============================================================================
# Updating
#============================================================================

# AeoLis
print 'AeoLiS'
print 'start time is', AL_model.get_current_time()
AL_model.update()
print 'time step is', AL_model.get_var('dt')
print 'new time is', AL_model.get_current_time()

# DFlow
print 'D-Flow FM'
print 'start time is', DF_wrapper.get_current_time()
DF_wrapper.update(DF_wrapper.get_time_step())
print 'new time is', DF_wrapper.get_current_time()
# update until Dflow time matches Aeolis time
while DF_wrapper.get_current_time()<AL_model.get_current_time():
    DF_wrapper.update(DF_wrapper.get_time_step())
print 'time step is', DF_wrapper.get_time_step()
print 'new time is', DF_wrapper.get_current_time()

#==============================================================================
# Finalizing
#============================================================================

AL_model.finalize()
DF_wrapper.finalize()
