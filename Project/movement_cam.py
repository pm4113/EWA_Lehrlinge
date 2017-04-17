def azimut_up(dc_azimut):
        dc_azimut += 0.2
        if dc_azimut >= 30:
                dc_azimut = 30
#        print "DC_UP: " + str(dc_azimut)
        return dc_azimut

def azimut_down(dc_azimut):
        dc_azimut -= 0.2
        if dc_azimut <= 0:
                dc_azimut = 0
#        print "DC_DOWN: " + str(dc_azimut)
        return dc_azimut

def elevation_up(dc_elevation):
        dc_elevation += 0.2
        if dc_elevation >= 30:
                dc_elevation = 30
#        print "DC_UP: " + str(dc_elevation)
        return dc_elevation

def elevation_down(dc_elevation):
        dc_elevation -= 0.2
        if dc_elevation <= 0:
                dc_elevation = 0
#        print "DC_DOWN: " + str(dc_elevation)
        return dc_elevation
