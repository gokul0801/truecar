import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'truecar.settings'
django.setup()
from vehicles.models import Vehicle, VSNPattern
from collections import defaultdict
import fnmatch, optparse, re

HEADER_RE = re.compile('^Serial Number Pattern')

### Read Vehical Serial Number patterns from csv file and
### store them in the vehicles database
def load_patterns(opts):
  f = file(opts.filename)

  for line in f:
     if not HEADER_RE.search(line):
	line = line.strip()
        columns = line.split(',')
	input_pattern = columns[0]
	trim_id = columns[1]
	print "Reading VSN pattern %s, Vehicle Trim Id %s" % (input_pattern, trim_id)
	vehicle, created = Vehicle.objects.get_or_create(trim_id = trim_id,
						 year = columns[2],
						 make = columns[3],
					         model = columns[4],
				                 trim_name = columns[5])
	
	if created:
	   print "Created vehicle object: " + str(vehicle)
	vsnPattern, created = VSNPattern.objects.get_or_create(pattern = input_pattern, vehicle = vehicle)
	if created:
	   print "Created VSNPattern object: " + str(vsnPattern)

  f.close()
			           
 
if '__main__' == __name__:
   parser = optparse.OptionParser()
   parser.add_option('-f', '--file', dest='filename', help='VSN Pattern csv file')
   opts, args = parser.parse_args()
   load_patterns(opts)
