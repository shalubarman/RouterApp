from django.core.management.base import BaseCommand, CommandError
import string,random
from router.models import Router
from django.db import IntegrityError

# from polls.models import Question as Poll

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('count')

    def handle(self, *args, **options):

        n = int(options['count'])
        

        for i in range(n):
            try:
                sapid = self.generate_random_sapid()
                hostname = self.generate_random_hostname()
                loopback = self.generate_random_loopback()
                mac = self.generate_random_mac()
                #self.stdout.write(sapid + '=' + hostname + '=' + loopback + '=' + mac)
                router = Router(sapid = sapid, hostname = hostname, loopback = loopback, mac = mac)
                router.save()
            except Exception as e:
                self.stdout.write(e)
        
            


    def generate_random_hostname(self):
        s = string.uppercase + string.digits
        r = ''.join(random.choice(s) for i in range(14))
        return r

    def generate_random_sapid(self):
        len_list = [1,2,4,3]
        res_list = []
        for t in len_list:
            q = ''.join(random.choice(string.uppercase) for l in range(t))
            res_list.append(q)
        n = ''.join(random.choice(string.digits) for l in range(4))
        res_list.append(n)
        r = '-'.join(res_list)
        return r

    def generate_random_loopback(self):
        r = '.'.join(str(random.randint(0,255)) for l in range(4))
        return r

    def generate_random_mac(self):
        res_list = []
        for t in range(6):
            q = ''.join(random.choice(string.hexdigits) for l in range(2))
            res_list.append(q)
        r = ':'.join(res_list)
        return r





