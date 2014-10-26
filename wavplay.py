import os
from wave import open as waveOpen
from ossaudiodev import open as ossOpen
from ossaudiodev import AFMT_S16_NE

def wav_to_dsp(wav_path):

    try:
        s = waveOpen(wav_path, 'rb')
        dsp = ossOpen('/dev/dsp','w')
        nc, sw, fr, nf, comptype, compname = s.getparams()
        dsp.setparameters(AFMT_S16_NE, nc, fr)
        data = s.readframes(nf)
        dsp.write(data)
    finally:
        for obj in s, dsp:
            try:
                getattr(obj, 'close')()
            except Exception:
                pass
