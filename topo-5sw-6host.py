"""Custom topology example

Two directly connected switches plus a host for each switch:

		switch	    switch
		  |	       |
		--------------------
		|	 |	   |
            switch     switch    switch 
	      |	 	 |	   |
	    host	host      host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts 
        leftleftHost = self.addHost( 'h1' )
	leftHost = self.addHost( 'h2' )
	middleleftHost = self.addHost( 'h3' )
	middlerightHost = self.addHost( 'h4' )
        rightHost = self.addHost( 'h5' )
	rightrightHost = self.addHost( 'h6' )

	# Add  switches
        leftupSwitch = self.addSwitch( 'sul1' )
        rightupSwitch = self.addSwitch( 'sur2' )
	leftdownSwitch = self.addSwitch( 'sdl3' )
	middledownSwitch = self.addSwitch( 'sdm4' )
	rightdownSwitch = self.addSwitch( 'sdr5' )

        # Add links hosts-switches
        self.addLink( leftleftHost, leftdownSwitch )
	self.addLink( leftHost, leftdownSwitch )
        self.addLink( middleleftHost, middledownSwitch )
	self.addLink( middlerightHost, middledownSwitch )
        self.addLink( rightHost, rightdownSwitch )
	self.addLink( rightrightHost, rightdownSwitch )
	
	# Add links switches-switches
	self.addLink( leftupSwitch, rightupSwitch )
	self.addLink( leftupSwitch, leftdownSwitch )
	self.addLink( rightupSwitch, leftdownSwitch )
	self.addLink( leftupSwitch, middledownSwitch )
	self.addLink( rightupSwitch, middledownSwitch )
	self.addLink( leftupSwitch, rightdownSwitch )
	self.addLink( rightupSwitch, rightdownSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }
