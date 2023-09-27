import logging

'''

'''

def factorial(n):
    logging.debug('Start of factorial(%s)'  % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is number ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)'  % (n))
    return total

if __name__=='__main__':
    #logging.basicConfig(level=logging.DEBUG,format='%(asctime)s -  %(levelname)s -  %(message)s')
    logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
    logging.debug('Start of program')
    print(factorial(5))
    logging.debug('End of Program')
    logging.debug('Some debugging details.')
    logging.info('The logging module is working.')
    logging.warning('An error message is about to be logged.')
    logging.error('An error has occurred.')
    logging.critical('The program is unable to recover!')
    logging.critical('Critical error! Critical error!')

    
    '''
        Since logging.disable() will disable all messages after it, you will probably want to add it near the import logging line of code in your program. 
        This way, you can easily find it to comment out or uncomment that call to enable or disable logging messages as needed.
    '''
    #logging.disable(logging.CRITICAL)
    logging.critical('Critical error! Critical error!')
    logging.error('Error! Error!')
