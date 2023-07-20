import streamlit as st 
import os,sys
import numpy as np
import pandas as pd 
from profiling_frame import *
import subprocess
from trycatch.exception import SystemException
from trycatch import logger



class perform_eda:
    
    try:
        def __init__(self):
            cmd = 'streamlit run profiling_frame.py'
            subprocess.run(cmd, shell=True)         
    except Exception as e:
        raise SystemException(e,sys)
        