from hdmf.backends.hdf5.h5_utils import H5DataIO
import numpy as np

class WrappedData:

    def __init__(self):
        pass

    def create_acq_device(nwbfile, header):
        """Create a `device` object in the NWB file for the headstage/amplifier
        system the data was acquired with.

        Parameters
        ----------
        nwbfile : pynwb.NWBFile
            The NWB file to create the device in.
        header : dict
            Dictionary containing WaveSurfer metadata.

        Returns
        -------
        pynwb.device.Device
            NWB device representing acquisition object.
        """
        device = nwbfile.create_device(name=header['device']['name'],
                                       description=header['device']['description'])
        return device