import config_pulse_gen as config
import sys
# import os

argvs = sys.argv

if len(argvs) != 6:
    print('Usage: python configuration.py  fre=50 amp=1.8 delay=5 sync=CH2 comb=True ' )
    sys.exit()

fre =  int(sys.argv[1] )
amp =  float(sys.argv[2] )
delay =  int(sys.argv[3] )
sync =  str(sys.argv[4] )
comb =  sys.argv[5] 

if comb == 'True':
    config.configure_waveform_generator(fre, amp, delay, sync, True)
elif comb == 'False':
    config.configure_waveform_generator(fre, amp, delay, sync, False)




config.pulse_generator_configure()

sys.exit()
