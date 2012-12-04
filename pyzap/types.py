
from ctypes import *

class TUNER_DESCRIPTOR(Structure):
    _fields_ = [('adapter',  c_uint),
                ('frontend', c_uint),
                ('demux',    c_uint),
               ]

class ATSC_TUNE_INFO(Structure):
    _fields_ = [('frequency',  c_uint),
                ('modulation', c_uint),
                ('vpid',       c_uint),
                ('apid',       c_uint),
               ]

class DVBC_TUNE_INFO(Structure):
    _fields_ = [('frequency',        c_uint),
                ('modulation',       c_uint),
                ('vpid',             c_uint),
                ('apid',             c_uint),
                ('sid',              c_uint),
                ('inversion',        c_uint),
                ('sym_per_sec',      c_uint),
                ('forward_err_corr', c_uint),
               ]

class DVBS_TUNE_INFO(Structure):
    _fields_ = [('frequency', c_uint),
                ('vpid',      c_uint),
                ('apid',      c_uint),
                ('sid',       c_uint),
                ('pol',       c_uint),
                ('sat_no',    c_uint),
                ('sr',        c_uint),
               ]

class DVBT_TUNE_INFO(Structure):
    _fields_ = [('frequency',             c_uint),
                ('modulation',            c_uint),
                ('vpid',                  c_uint),
                ('apid',                  c_uint),
                ('sid',                   c_uint),
                ('inversion',             c_uint),
                ('bandwidth',             c_uint),
                ('forward_err_corr_hp',   c_uint),
                ('forward_err_corr_lp',   c_uint),
                ('transmission_mode',     c_uint),
                ('guard_interval',        c_uint),
                ('heirarchy_information', c_uint),
               ]

STATUS_RECEIVER_CB = CFUNCTYPE(c_int, 
							   c_int, 
							   c_ushort, 
							   c_ushort, 
							   c_uint, 
							   c_uint, 
							   c_uint
							  )



