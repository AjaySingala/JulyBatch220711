import logging

# Default logging level is WARNING.
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# print("\nChange default logging level...")
# # Change logging level to DEBUG.
# # Comment code above first.
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# # Logging to a file.
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')
# logging.error('This will get logged to a file')
# logging.critical('This will get logged to a file')

# # Formatting the output.
# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.warning('This is a Warning')

# # Add date-time.
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')

# # Another example to format date-time with %(asctime) and datefmt.
# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')

# # Log variable dats.
# name = 'John'
# logging.error('%s raised an error', name)
# logging.error(f'{name} raised an error')

# # Capture stack trace.
# a = 5
# b = 0
# try:
#     c = a / b
# except Exception as e:
#     logging.error("Exception occurred", exc_info=True)

# # Use logging.exception if using try-except.
# a = 5
# b = 0
# try:
#     c = a / b
# except Exception as e:
#     logging.exception("Exception occurred")

# # Custom logger object.
# logger = logging.getLogger('example_logger')
# logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')
# logger.warning('This is a warning')
# ## Uncomment first set of logging commands and check output.
