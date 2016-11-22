#
# Copyright 2005-2016 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.
#

import traceback
import sys

from gribapi import *

INPUT = '../../data/reduced_gaussian_lsm.grib1'
VERBOSE = 1  # verbose error reporting


def example():
    points = ((30, -20), (13, 234))

    f = open(INPUT)
    gid = grib_new_from_file(f)

    for lat, lon in points:
        nearest = grib_find_nearest(gid, lat, lon)[0]
        print lat, lon
        print nearest.lat, nearest.lon, nearest.value, nearest.distance, nearest.index

        four = grib_find_nearest(gid, lat, lon, is_lsm=False, npoints=4)
        for i in range(len(four)):
            print "- %d -" % i
            print four[i]

        print "-" * 100

    grib_release(gid)
    f.close()


def main():
    try:
        example()
    except GribInternalError, err:
        if VERBOSE:
            traceback.print_exc(file=sys.stderr)
        else:
            print >>sys.stderr, err.msg

        return 1

if __name__ == "__main__":
    sys.exit(main())
