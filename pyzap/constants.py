"""Emulate the standard constants defined in 
<include-dir>/linux/dvb/frontend.h . Most/all of these were, originally, enums.
"""

_modulations = [
	'QPSK',
	'QAM_16',
	'QAM_32',
	'QAM_64',
	'QAM_128',
	'QAM_256',
	'QAM_AUTO',
	'VSB_8',
	'VSB_16',
	'PSK_8',
	'APSK_16',
	'APSK_32',
	'DQPSK',
]

def modulation(name):
    return _modulations.index(name)

_spectral_inversion = [
	'INVERSION_OFF',
	'INVERSION_ON',
	'INVERSION_AUTO',
]

def spectral_inversion(name):
    return __spectral_inversion.index(name)

_code_rate = [
	'FEC_NONE',
	'FEC_1_2',
	'FEC_2_3',
	'FEC_3_4',
	'FEC_4_5',
	'FEC_5_6',
	'FEC_6_7',
	'FEC_7_8',
	'FEC_8_9',
	'FEC_AUTO',
	'FEC_3_5',
	'FEC_9_10',
]

def code_rate(name):
    return __code_rate.index(name)

