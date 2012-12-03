from ctypes import *
from os import environ

library_filepath = environ['ZAPLIB_FILEPATH'] \
                    if 'ZAPLIB_FILEPATH' in environ \
                    else '/usr/lib/zaplib.so'

instance = cdll.LoadLibrary(library_filepath)

#typedef int (*StatusReceiver)(fe_status_t status, uint16_t signal, uint16_t snr, uint32_t ber, uint32_t uncorrected_blocks, int is_locked);

C_STATUS_RECEIVER = CFUNCTYPE(c_int, 
							  c_int, 
							  c_ushort, 
							  c_ushort, 
							  c_uint, 
							  c_uint, 
							  c_uint
							 )

#int azap_tune_silent(int frequency, fe_modulation_t modulation, int vpid, 
#                     int apid, int adapter, int frontend, int demux, int dvr, 
#                     StatusReceiver statusReceiver)

c_azap_tune_silent = instance.azap_tune_silent
c_azap_tune_silent.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int, 
                               c_int, C_STATUS_RECEIVER]
c_azap_tune_silent.restypes = c_int

#int czap_tune_silent(int adapter, int frontend, int demux, int dvr, 
#                     int frequency, int vpid, int apid, int sid, int inversion, 
#                     int sym_per_sec, int modulation, int forward_err_corr, 
#                     int rec_psi, StatusReceiver statusReceiver);

c_czap_tune_silent = instance.czap_tune_silent
c_czap_tune_silent.argtypes = [c_int, c_int, c_int, c_int, 
                               c_int, c_int, c_int, c_int, c_int,
                               c_int, c_int, c_int,
                               c_int, C_STATUS_RECEIVER]
c_czap_tune_silent.restypes = c_int

