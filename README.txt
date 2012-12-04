!! IMPORTANT !!
===============

(1)

Although I have implemented the DVB-C wrapper, it has not yet been tested. It
will be tested shortly.

(2)

As I only have access to ATSC and DVB-C transmissions, I have not written the 
wrappers for DVB-S (satellite) and DVB-T (terrestrial.. non-US?). Writing these
wrappers is a trivial exercise:

> Writing a CTYPES prototype in Python for the header of the corresponding 
  tuning function in ZapLib.
> Defining any undefined constants/ENUMs required by the structs of that header 
  and missing in pyzap.constants . 
  > These constants represent those defined in the kernel header 
    linux/dvb/frontend.h .

If anyone has the -S and -T sources available to them, I'd be happy to 
implement them, with those users' help.

Summary
=======

Python wrapper library for ZapLib digital television (DVB) tuning library.

Description
===========

This library allows a Python script to tune channels with nothing more than the 
ZapLib library, and the correct tuning values for the type of DVB that you're
trying to decode. No channels.conf file is required.

ATSC (air/US) Example
=====================

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

To execute when zaplib.so is in a non-standard location:

    ZAPLIB_FILEPATH=~/development/c/zaplib/zaplib.so ./test.py

