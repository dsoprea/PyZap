from ctypes import *
from os import environ
from os.path import exists

from pyzap.types import *

if 'ZAPLIB_FILEPATH' in environ:
    library_filepath = environ['ZAPLIB_FILEPATH']
elif exists('/usr/local/lib/libzaplib.so'):
    library_filepath = '/usr/local/lib/libzaplib.so'
elif exists('/usr/lib/libzaplib.so'):
    library_filepath = '/usr/lib/libzaplib.so'
else:
    raise SystemError("Could not determine path of libzaplib.so .")

instance = cdll.LoadLibrary(library_filepath)

#extern int azap_tune_silent(t_tuner_descriptor tuner, 
#                            t_atsc_tune_info tune_info, int dvr, int rec_psi,
#                            StatusReceiver statusReceiver);

c_azap_tune_silent = instance.azap_tune_silent
c_azap_tune_silent.argtypes = [TUNER_DESCRIPTOR, ATSC_TUNE_INFO, c_int, c_int,
                               STATUS_RECEIVER_CB]
c_azap_tune_silent.restypes = c_int

#extern int czap_tune_silent(t_tuner_descriptor tuner, 
#                            t_dvbc_tune_info tune_info, int dvr, int rec_psi, 
#                            StatusReceiver statusReceiver);

c_czap_tune_silent = instance.czap_tune_silent
c_czap_tune_silent.argtypes = [TUNER_DESCRIPTOR, DVBC_TUNE_INFO, c_int, c_int,
                               STATUS_RECEIVER_CB]
c_czap_tune_silent.restypes = c_int

#extern int szap_tune_silent(t_tuner_descriptor tuner, 
#                            t_dvbs_tune_info tune_info, int dvr, 
#                            unsigned int rec_psi, 
#                            StatusReceiver statusReceiver, int audio_bypass, 
#                            char *lnb_raw)

c_szap_tune_silent = instance.szap_tune_silent
c_szap_tune_silent.argtypes = [TUNER_DESCRIPTOR, DVBS_TUNE_INFO, c_int, c_int,
                               STATUS_RECEIVER_CB, c_int, c_char_p]
c_szap_tune_silent.restypes = c_int

#extern int tzap_tune_silent(t_tuner_descriptor tuner, t_dvbt_tune_info tune_info, 
#                            int dvr, unsigned int rec_psi, 
#                            StatusReceiver statusReceiver)

c_tzap_tune_silent = instance.tzap_tune_silent
c_tzap_tune_silent.argtypes = [TUNER_DESCRIPTOR, DVBS_TUNE_INFO, c_int, c_int,
                               STATUS_RECEIVER_CB]
c_tzap_tune_silent.restypes = c_int

