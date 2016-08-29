# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:53:44 2016

@author: velhorst
"""

from bmi.wrapper import BMIWrapper
BMIWrapper.known_paths.append(r'C:/vanArjen-Dflow_setup/fm_versions/16Aug/win64/dflowfm') #set path to library
BMIWrapper.known_paths.append(r'C:/vanArjen-Dflow_setup/fm_versions/16Aug/win64/wave/bin')
BMIWrapper.known_paths.append(r'C:/vanArjen-Dflow_setup/fm_versions/16Aug/win64/esmf/bin')
BMIWrapper.known_paths.append(r'C:/vanArjen-Dflow_setup/fm_versions/16Aug/win64/swan/bin')
# print BMIWrapper.known_paths

mdu_file = r'C:/vanArjen-Dflow_setup/Zandmotor_FM_Aug2016_run06_BMIwrapper_try_waves/fm/zm_dfm.mdu' # set path to ini file

wrapper = BMIWrapper(engine="dflowfm", configfile=mdu_file)

# run the model
wrapper.initialize()

print wrapper.get_end_time()
print wrapper.get_time_step()

# playing with the update function
#wrapper.update(1.0)
#print wrapper.get_current_time()
#wrapper.update(10.0)
#print wrapper.get_current_time()
#wrapper.update(100.0)
#print wrapper.get_current_time()

# Using a for loop to update a few timesteps
#for timesteps in range(20):
#    wrapper.update(wrapper.get_time_step())
#    print wrapper.get_current_time()

# Using a while to update through all the timesteps
while wrapper.get_current_time()<wrapper.get_end_time():
    wrapper.update(wrapper.get_time_step())
#    print wrapper.get_current_time()


wrapper.finalize()
