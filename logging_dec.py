import datetime

def logging_decorator(func):
  def log_fn():
    print 'Executing ' + func.__name__ + '...'
  
  log_fn()
  return func
