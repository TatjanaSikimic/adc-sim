# adc-sim
A simulated Python Air Data Computer (ADC) that ingests data from three redundant pressure and temperature sensors, applies median voting for fault detection and isolation (FDI), computes altitude, airspeed (IAS/TAS), and vertical speed via the ISA model, and broadcasts outputs over UDP in a simplified ARINC 429 format.
