#!/bin/bash
gunicorn -w 4 madzones.wsgi -b 0.0.0.0:80 

