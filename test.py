import httplib
import re
import subprocess
import time


class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_test_file():
    conn = httplib.HTTPConnection('127.0.0.1', 8080)
    conn.request('GET', '/shibboleth-ds/idpselect_config.js')
    response = conn.getresponse()
    data = response.read()
    return (response.status, len(data))


def test_image(image_name):
    container_name = 'eds'
    print 'Launching %s' % (image_name)
    status = subprocess.call(['docker', 'run', '-d', '-p', '8080:80', '--rm',
                              '--name', container_name, image_name])
    print 'Launch status: %r' % (status)
    time.sleep(5)
    print 'get_test_file: response %d; data len %d' % get_test_file()
    print 'Stopping %s' % (image_name)
    status = subprocess.call(['docker', 'stop', container_name])
    print 'Stop status: %r' % (status)


for repo in ['eds', 'eds80']:
    for tag in ['centos6', 'centos7']:
        image_name = '%s:%s' % (repo, tag)
        test_image(image_name)
