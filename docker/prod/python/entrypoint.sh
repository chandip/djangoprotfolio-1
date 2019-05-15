##!/bin/bash
#
#echo "Running command '$*'"
#exec /bin/bash -c "$*"

#!/bin/bash
gunicorn -w 4 madzones.wsgi -b 0.0.0.0:80