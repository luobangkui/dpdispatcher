import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from dpgen.dispatcher.Dispatcher import Dispatcher
from dpgen.dispatcher.JobStatus import JobStatus
from dpgen.dispatcher.LazyLocalContext import LazyLocalContext
from dpgen.dispatcher.LocalContext import LocalContext, LocalSession
from dpgen.dispatcher.Slurm import Slurm
from dpgen.dispatcher.SSHContext import SSHContext, SSHSession


def my_file_cmp(test, f0, f1):
    with open(f0) as fp0:
        with open(f1) as fp1:
            test.assertTrue(fp0.read() == fp1.read())


def setUpModule():
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
