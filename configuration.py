import config_pulse_gen as config
import sys

argvs = sys.argv
if len(argvs) < 4:
    print('Usage: python configuration.py  fre=50 amp=1.8 offset=0.9 delay=5')
    sys.exit()
fre =  int(sys.argv[1] )
amp =  float(sys.argv[2] )
offset =  float(sys.argv[3] )
delay =  int(sys.argv[4] )

config.configure_waveform_generator(fre, amp, offset, delay)


config.pulse_generator_configure()

sys.exit()
