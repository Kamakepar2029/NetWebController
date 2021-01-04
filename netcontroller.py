import os
import json

class NetController():
    def __init__(self):
        self.net_conf = ''
    
    def load_config(self, config):
        if config != '':
            try:
                self.net_conf == open(config,'r').read()
                pass
            except:
                pass
    def get_ports(self,nows):
        mynow = os.popen('netstat -nltp').read()
        mass = mynow.split('\n')
        #print(mass)
        stringfds = ''
        jsonready = []
        name = 0
        pol = 0
        allsdf = []
        jsonnot = {}
        for line in mass:
            mass_all = line.split(' ')
            for me in mass_all:
                if me != '':
                    if me == 'name':
                        name +=1

                    if name ==1:
                        pol+=1
                        if pol >1:
                           allsdf.append(me)

        #['tcp', '0', '0', '0.0.0.0:902', '0.0.0.0:*', 'LISTEN', '1373/vmware-authdla', 
        # 'tcp', '0', '0', '127.0.0.1:40981', '0.0.0.0:*', 'LISTEN', '15157/vscodium', 
        # 'tcp', '0', '0', '127.0.0.1:631', '0.0.0.0:*', 'LISTEN', '567/cupsd', 
        # 'tcp', '0', '0', '0.0.0.0:7070', '0.0.0.0:*', 'LISTEN', '752/anydesk', 
        # 'tcp6', '0', '0', ':::902', ':::*', 'LISTEN', '1373/vmware-authdla', 
        # 'tcp6', '0', '0', '::1:631', ':::*', 'LISTEN', '567/cupsd']
        start = 0
        end = len(allsdf)-1
        while start<end:
            if start%7 == 0:
                jsonnot = {}
                jsonnot["type"] = allsdf[start-7]
                jsonnot["recvq"] = allsdf[start-6]
                jsonnot["sendq"] = allsdf[start-5]
                jsonnot["hostport"] = allsdf[start-4]
                jsonnot["host"] = allsdf[start-3]
                jsonnot["typli"] = allsdf[start-2]
                namepidmass = allsdf[start-1].split('/')
                jsonnot["pid"] = namepidmass[0]
                jsonnot["name"] = namepidmass[1]
                jsonready.append(jsonnot)
            start+=1
        return str(jsonready).replace("'",'"')