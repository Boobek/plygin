from .. import plugin

'''
This file is the plugin itself
'''

class Plugin(plugin.Plugin):
    def __init__(self, Meta):
        plugin.Plugin.__init__(self, Meta)

    def execute(self):
        print "EXECUTED"
