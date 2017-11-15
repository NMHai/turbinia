#!/usr/bin/env python

import subprocess
import sys

from turbinia import config

index_file = './index.yaml'

if len(sys.argv) > 1:
  function_names = [sys.argv[1]]
else:
  function_names = ['gettasks', 'getrecenttasks']

config.LoadConfig()

for function in function_names:
  print 'Deploying function {0:s}'.format(function)
  cmd = ('gcloud beta functions deploy {0:s} --stage-bucket {1:s} '
         '--trigger-http'.format(function, config.BUCKET_NAME))
  print subprocess.check_call(cmd, shell=True)

print '/nCreating Datastore index from {0:s}'.format(index_file)
cmd = 'yes | gcloud datastore create-indexes {0:s}'.format(index_file)
subprocess.check_call(cmd, shell=True)
