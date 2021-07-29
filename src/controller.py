from blinker import Signal
from collections import namedtuple
from db import myDb


class controller:
    # of slaves
    UNITNAMES=["termUI","db","prog"]
    def __init__(self):

        self._Units=namedtuple("units",self.UNITNAMES)

        self._init_signals()
        self._init_packets()
        self._init_units()

        self._subscribe_to_units()

    def _init_signals(self):
        e=[Signal()]*len(self.UNITNAMES)
        self.signals=self._Units(*e)

    def _init_packets(self):
        e=[__packet()]*len(self.UNITNAMES)
        self.packets=self._Units(*e)

    def _init_units(self):
        self.units=Units(termUI(self),myDB(self))

    def _subscribe_to_units(self):
        for sig in range(len(self.units)):
            sig.connect(self._parse_msg)

    def get_unit_ind(self, unitName):
        return self.UNITNAMES.index(unitName)

    def send_msg(dest,msg,**kwargs):
        ind=self.get_ind(dest)
        result=self.packets[ind].sig.send(msg,**kwargs);

    def _parse_msg(self,packet):
        msg=packet[1]
        kwargs=packet[2]
        print(msg) #msg


class slave:
    # to the controller
    def __init__(self,contr):
        self._slave_name_=self.__class__.__bases__[-1] # XXX CHECK IF WORKS
        self._contr_ind_=contr.get_unit_ind(self._slave_name_)

        # subscribe to controller
        contr.signals[self._contr_ind_].connect(self.parse_msg)

        # create signal packet
        self._packet_=__packet(self.slave_name)

    def send_msg(msg,**kwargs):
        result=self._packet_.sig.send(msg,**kwargs);

    def parse_msg(self,packet):
        msg=packet[1]
        kwargs=packet[2]
        print(msg) # msg


class __packet:
    def __init__(self,*argv):
        if len(argv) > 0:
            self.init(name)

    def init(self,name):
        self.sig=signal(name) # signal is senders name

        @sig.connect # on connect ...
        def open(msg,**kwargs):
            return (msg,kwargs) # return message & keypairs
