#!/usr/bin/python

from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo


class FatTreeTopo(Topo):

    """ Switch-Routed (Fat Tree) Topology """

    def __init__(self):

        """ Constructor for creating the Switched Routed Topology """

        Topo.__init__(self)

        # Adding the ToR Switches
        switch1 = self.addSwitch('switch1', cls=OVSKernelSwitch)
        switch2 = self.addSwitch('switch2', cls=OVSKernelSwitch)
        switch3 = self.addSwitch('switch3', cls=OVSKernelSwitch)
        switch4 = self.addSwitch('switch4', cls=OVSKernelSwitch)

        # Adding the Aggregate Switches
        switch21 = self.addSwitch('switch21', cls=OVSKernelSwitch)
        switch10 = self.addSwitch('switch10', cls=OVSKernelSwitch)
        switch11 = self.addSwitch('switch11', cls=OVSKernelSwitch)
        switch22 = self.addSwitch('switch22', cls=OVSKernelSwitch)

        # Adding the Core Switches
        switch17 = self.addSwitch('switch17', cls=OVSKernelSwitch)
        switch18 = self.addSwitch('switch18', cls=OVSKernelSwitch)

        # Adding hosts for the ToR Switch 1
        host1 = self.addHost('host1', cls=Host, ip='10.1.1.1', defaultRoute=None)
        host2 = self.addHost('host2', cls=Host, ip='10.1.1.2', defaultRoute=None)

        # Adding hosts for the ToR Switch 2
        host3 = self.addHost('host3', cls=Host, ip='10.1.1.3', defaultRoute=None)
        host4 = self.addHost('host4', cls=Host, ip='10.1.1.4', defaultRoute=None)

        # Adding hosts for the ToR Switch 3
        host5 = self.addHost('host5', cls=Host, ip='10.1.1.5', defaultRoute=None)
        host6 = self.addHost('host6', cls=Host, ip='10.1.1.6', defaultRoute=None)

        # Adding hosts for the ToR Switch 4
        host7 = self.addHost('host7', cls=Host, ip='10.1.1.7', defaultRoute=None)
        host8 = self.addHost('host8', cls=Host, ip='10.1.1.8', defaultRoute=None)

        # Add links
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch2)
        self.addLink(host4, switch2)
        self.addLink(host5, switch3)
        self.addLink(host6, switch3)
        self.addLink(host7, switch4)
        self.addLink(host8, switch4)
        self.addLink(switch1, switch21)
        self.addLink(switch21, switch2)
        self.addLink(switch1, switch10)
        self.addLink(switch2, switch10)
        self.addLink(switch3, switch11)
        self.addLink(switch4, switch22)
        self.addLink(switch11, switch4)
        self.addLink(switch3, switch22)
        self.addLink(switch21, switch17)
        self.addLink(switch11, switch17)
        self.addLink(switch10, switch18)
        self.addLink(switch22, switch18)

topos = {'mytopo': (lambda: FatTreeTopo())}
