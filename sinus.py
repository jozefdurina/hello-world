import math

for angle_in_deg in range(0, 361, 10):
    angle_in_rad = math.radians ( angle_in_deg )
    sinus = math.sin ( angle_in_rad )
    odskok = int ( 40 + 35 * sinus )
    print ( ' ' * odskok + 'SINUS')
