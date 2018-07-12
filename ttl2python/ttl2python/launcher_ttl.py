import pexpect
import sys
import getpass
import logging
import os
 
SSH_NEWKEY = r'Are you sure you want to continue connecting \(yes/no\)\?'

def send_cmd(child, prompt, cmd):
    child.expect(prompt)
    child.sendline(cmd)

def send_password(child, password):
    i = child.expect([pexpect.TIMEOUT, SSH_NEWKEY, '[Pp]assword: '])
    if i == 0: # Timeout
        print('ERROR!')
        print('SSH could not login. Here is what SSH said:')
        print(child.before, child.after)
        sys.exit(1)
    if i == 1: # SSH does not have the public key.  Just accept it.
        child.sendline('yes')
        child.expect('[Pp]assword:')

    child.sendline(password)
 

def ttlParse(filename):
    f = open(filename)
    child = None
    waitKeywords = None
    isIfIgnore = False
    prevWaitId = -1
    lastIfIndex = -1
    for lineStr in f.readlines():
        str = lineStr.strip()
        str = str.replace('\'','')

        lineArray = str.split(' ')
        
        if(isIfIgnore):
            logging.debug('search endif==================')
            if('endif' in lineArray):
                logging.debug('endif')
                lastIfIndex = -1
                isIfIgnore = False
            else:
                logging.debug('not endif')
            continue

        if('connect' in lineArray):
            logging.debug('connect==================')
            str = ''.join(lineArray).replace('/','').split(' ')
            host = lineArray[1].split(':')
            host = host[0]

            for i in lineArray :
                re = i.split('=')
                logging.debug(re)
                if '/user' in re:
                    user = re[1]
                    continue
                if '/passwd' in re:
                    passwd = re[1]
        
            logging.debug('%s,%s,%s' % (host, user, passwd))
            ofp = open('foo.out','w')
            child = pexpect.spawn('ssh %s@%s' % (user, host), logfile=ofp)
            send_password(child, passwd)
            continue

        if('wait' in lineArray):
            logging.debug('wait==================')
            waitKeywords = lineArray[1:]
            logging.debug(waitKeywords)
            if lastIfIndex == -1:
                prevWaitId = child.expect_exact(waitKeywords)
            else:
                child.expect_exact(waitKeywords)
            logging.debug('select : %s' % prevWaitId)
            continue

        if('sendln' in lineArray):
            logging.debug('sendln==================')
            sendKeyword = ' '.join(lineArray[1:]).strip()
            logging.debug(sendKeyword)
            child.sendline(sendKeyword)
            continue

        if('if' in lineArray):
            logging.debug('if==================')
            res = lineArray[1].split('=')
            logging.debug(res)
            if 'result' in res:
                result = int(res[1]) - 1
            
            logging.debug(result)
            logging.debug(prevWaitId)
            #print waitKeywords[prevWaitId]
            
            if prevWaitId == result :
                lastIfIndex = prevWaitId
                logging.debug('OK')
            else :
                logging.debug('NOT OK')
                #print waitKeywords
                #print '%s = %s' % (waitKeywords[result],
                #waitKeywords[prevWaitId])
                isIfIgnore = True
            continue
        
    child.sendline()    
    child.interact()
    child.close()



if __name__ == '__main__' :
    logging.basicConfig(level=logging.DEBUG)

    dirpath = os.path.realpath(os.path.dirname(__file__)) + '/ttl'
    files = [file for file in os.listdir(dirpath) if file.endswith(".ttl")]
    files.sort()
    index = 1

    for name in files:
        print('%d. %s' % (index, name))
        index = index + 1
       
    print 'select ttl : ',
    index = input() 
    ttlParse('%s/%s' % (dirpath, files[int(index)-1]))
