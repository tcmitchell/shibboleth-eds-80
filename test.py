#!/usr/bin/env python

import httplib
import re
import subprocess
import time

import edsimage


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
    return (response.status, response.reason)


def test_image(image_name):
    container_name = 'eds'
    print '----------'
    print 'Launching %s' % (image_name)
    status = subprocess.call(['docker', 'run', '-d', '-p', '8080:80', '--rm',
                              '--name', container_name, image_name])
    if status is not 0:
        print 'Unable to launch image %s (status = %d)' % (image_name, status)
        return
    # Give Apache some time to start
    time.sleep(5)
    # Test the URL
    (http_status, data_len) = get_test_file()
    color = bcolors.OKGREEN
    if http_status is not 200:
        color = bcolors.FAIL
    msg = color + 'HTTP response: %d %s' + bcolors.ENDC
    print msg % (http_status, data_len)
    #
    # Stop the image
    print 'Stopping %s' % (image_name)
    status = subprocess.call(['docker', 'stop', container_name])
    if status != 0:
        print bcolors.FAIL + 'Stop status: %r' % (status) + bcolors.ENDC
    print


for tag in edsimage.TAGS:
    for repo in edsimage.REPOS:
        image_name = '%s:%s' % (repo, tag)
        test_image(image_name)
