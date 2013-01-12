from ctypes import *
from os import environ
from os.path import exists

from pyzap.types import *

if 'ZAPLIB_FILEPATH' in environ:
    library_filepath = environ['ZAPLIB_FILEPATH']
elif os.path.exists('/usr/local/lib/zaplib.so'):
    library_filepath = '/usr/local/lib/zaplib.so'
elif os.path.exists('/usr/lib/zaplib.so'):
    library_filepath = '/usr/lib/zaplib.so'
else
    raise SystemError("Could not determine path of zaplib.so .")

instance = cdll.LoadLibrary(library_filepath)

#extern int azap_tune_silent(t_tuner_descriptor tuner, 
#                            t_atsc_tune_info tune_info, int dvr, 
#                            StatusReceiver statusReceiver);

c_azap_tune_silent = instance.azap_tune_silent
c_azap_tune_silent.argtypes = [TUNER_DESCRIPTOR, ATSC_TUNE_INFO, c_int, 
                               STATUS_RECEIVER_CB]
c_azap_tune_silent.restypes = c_int

#extern int czap_tune_silent(t_tuner_descriptor tuner, 
#                            t_dvbc_tune_info tune_info, int dvr, int rec_psi, 
#                            StatusReceiver statusReceiver);

c_czap_tune_silent = instance.czap_tune_silent
c_czap_tune_silent.argtypes = [TUNER_DESCRIPTOR, DVBC_TUNE_INFO, c_int, c_int,
                               STATUS_RECEIVER_CB]
c_czap_tune_silent.restypes = c_int

