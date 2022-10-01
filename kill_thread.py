import ctypes
from threading import Thread

def kill_thread(thread:Thread) -> bool: 
    ''' Attempt to kill thread
    
    @prama thread [Thread]: Thread instance object.

    @return [bool]: True or False
    '''
    if isinstance(thread,Thread):
        return ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), ctypes.py_object(SystemExit)) == 1
    else:
        return False
