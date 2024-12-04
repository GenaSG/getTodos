#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import argparse
libdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(libdir)
sys.path.append(os.path.join(libdir,'lib'))

from main import get_tasks

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', dest='tasks_filter', default='', type=str, help='Custom filter.')
    args = parser.parse_args()
    print(get_tasks(args.tasks_filter, os.environ['TODOIST_API_TOKEN']))
