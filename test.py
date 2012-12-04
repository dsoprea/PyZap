#!/usr/bin/python

from pyzap.types import *
from pyzap.calls import *
from pyzap.constants import *

max_calls = 15

def status_receiver(status, signal, snr, ber, uncorrected_blocks, is_locked):
    global max_calls

    print("Status received.  STATUS= (%d)  SNR= (%d)  IS_LOCKED= [%s]" % 
          (status, snr, bool(is_locked)))

    max_calls -= 1

    return (1 if max_calls > 0 else 0)

c_status_receiver = STATUS_RECEIVER_CB(status_receiver)

tuner_info = TUNER_DESCRIPTOR()
tuner_info.adapter  = 0
tuner_info.frontend = 0
tuner_info.demux    = 0

tune_info = ATSC_TUNE_INFO()
tune_info.frequency  = 551028615 # 'Florida' channel.
tune_info.modulation = modulation('VSB_8')
tune_info.vpid       = 0x61 #97
tune_info.apid       = 0x63 #99

dvr = 1

retval = c_azap_tune_silent(tuner_info, tune_info, dvr, c_status_receiver)

