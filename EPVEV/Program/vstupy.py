from EPVEV.Program.Stoziar import System, ZemneLano
from EPVEV.Vypocty.Aproximovana import XY
import Vodic
import Stoziar


vodice = {
                                                    ##KSI TREBA ZMENIT!!! - NEPLATNE
    "434-AL1/56-ST1A"   : Vodic(D=28.8, RAC20=0.0666, ksi=0.86, pocet_vo_zvazku=3),
    
}

stoziare = {
    "2x400kV Donau N+0" : Stoziar(
        [
            System(XY(-13.6, 23.24), XY(-7.3, 23.24), XY(-9.6, 34.45)), 
            System(XY(13.6, 23.24), XY(7.3, 23.24), XY(9.6, 34.45)), 
        ], 
        [
            ZemneLano(XY(-12.10, 36.45)), 
            ZemneLano(XY(-12.10, 36.45))
        ]
    ),
}

