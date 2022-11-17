""" Electromagnetic waves units calculator
here the base functionality implemented
use emcalc in terminal
and emcalc-gui for graphic interface
"""

__version__ = '17.11.2022'
__author__ = 'Serhiy Kobyakov'

from scipy.constants import h as the_h
from scipy.constants import c as the_c
from scipy.constants import e as the_e
import math


def str_is_float(the_str: str) -> bool:
    try:
        float(the_str)
        return True
    except ValueError:
        return False


def get_round_unc(the_val: str) -> float:
    # get the rounding uncertainty from the float which is in string variable
    if '.' in the_val:
        digits = len(the_val) - the_val.index('.') - 1
    else:
        digits = 0
    return pow(10, -digits) * 0.5


def round_value(the_val, the_unc: float) -> str:
    # round the_val to the same place as two significant figures of the_unc
    dec_place = 1 - int(math.floor(math.log10(the_unc)))
    if dec_place < 0:
        dec_place = 0
    return '{1:.{0}f}'.format(dec_place, the_val)


def nm_to_cm(the_nm_val: str) -> str:
    # convert nm to cm^-1
    the_value = 1e7 / float(the_nm_val)
    the_unc = 1e7 * get_round_unc(the_nm_val) / (float(the_nm_val) ** 2)
    return round_value(the_value, the_unc)


def nm_to_ev(the_nm_val: str) -> str:
    # convert nm to eV
    scale = the_h * the_c / (1e-9 * the_e)
    the_value = scale / float(the_nm_val)
    the_unc = scale * get_round_unc(the_nm_val) / (float(the_nm_val) ** 2)
    return round_value(the_value, the_unc)


def cm_to_nm(the_cm_val: str) -> str:
    # convert cm^-1 to nm
    the_value = 1e7 / float(the_cm_val)
    the_unc = 1e7 * get_round_unc(the_cm_val) / (float(the_cm_val) ** 2)
    return round_value(the_value, the_unc)


def cm_to_ev(the_cm_val: str) -> str:
    # convert cm^-1 to eV
    scale = the_h * the_c / (1e-2 * the_e)
    the_value = scale * float(the_cm_val)
    the_unc = scale * get_round_unc(the_cm_val)
    return round_value(the_value, the_unc)


def ev_to_nm(the_ev_val: str) -> str:
    # convert eV to nm
    scale = the_h * the_c / (1e-9 * the_e)
    the_value = scale / float(the_ev_val)
    the_unc = scale * get_round_unc(the_ev_val) / (float(the_ev_val) ** 2)
    return round_value(the_value, the_unc)


def ev_to_cm(the_ev_val: str) -> str:
    # convert eV to cm^-1
    scale = 1e-2 * the_e / (the_h * the_c)
    the_value = scale * float(the_ev_val)
    the_unc = scale * get_round_unc(the_ev_val)
    return round_value(the_value, the_unc)


def nm_to_range(val: float) -> str:
    # returns the range name based on nm wavelength value
    if val < 10:
        return ''
    elif 10 <= val < 100:
        return 'Extreme ultraviolet (E-UV)'
    elif 100 <= val < 280:
        return 'Ultraviolet (UV-C)'
    elif 280 <= val < 315:
        return 'Ultraviolet (UV-B)'
    elif 315 <= val < 380:
        return 'Ultraviolet (UV-A)'
    elif 380 <= val < 780:
        return 'Visible light'
    elif 780 <= val < 1400:
        return 'Near infrared (IR-A)'
    elif 1400 <= val < 3000:
        return 'Short-wavelength infrared (IR-B)'
    elif 3000 <= val < 8000:
        return 'Mid-wavelength infrared (IR-C)'
    elif 8000 <= val < 15000:
        return 'Long-wavelength infrared (IR-C)'
    elif 15_000 <= val < 1000_000:
        return 'Far infrared (IR-C)'
    elif 1000_000 <= val < 10_000_000:
        return 'Microwaves, Extremely high frequency (EHF)'
    elif 10_000_000 <= val < 100_000_000:
        return 'Microwaves, Super high frequency (SHF)'
    elif 100_000_000 <= val < 1000_000_000:
        return 'Microwaves, Ultra high frequency (UHF)'
    elif 1000_000_000 <= val < 10_000_000_000:
        return 'Radio waves, Very high frequency (VHF)'
    elif 10_000_000_000 <= val < 100_000_000_000:
        return 'Radio waves, High frequency (HF)'
    elif 100_000_000_000 <= val < 1000_000_000_000:
        return 'Radio waves, Medium frequency (MF)'
    elif 1000_000_000_000 <= val < 10_000_000_000_000:
        return 'Radio waves, Low frequency (LF)'
    elif 10_000_000_000_000 <= val < 100_000_000_000_000:
        return 'Radio waves, Very low frequency (VLF)'
    elif 1000_000_000_000_000 <= val < 10_000_000_000_000_000:
        return 'Radio waves, Super low frequency (SLF)'
    elif 10_000_000_000_000_000 <= val < 100_000_000_000_000_000:
        return 'Radio waves, Extremely low frequency (ELF)'
    elif val >= 100_000_000_000_000_000:
        return ''
