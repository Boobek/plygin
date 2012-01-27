'''
This file is the meta descriptor of the plugin.
'''
class Meta(object):
    '''Name of the plugin (lowercase, without witespaces (str)'''
    name = "example-plugin"

    '''Version of the plugin (int)'''
    version = 1

    '''
    Required if @visible
    The name that visible in the action button (str)'''
    visibleName = "Working with example plugin"

    '''
    Required if @visible
    Description of the plugin (str)'''
    description = ''' This plugin is an example for  further works... '''

    '''This is optional.
    If the plugin activated by a menu element or a button in the starter screan or just a fastkey.
    The visibleName showed in that place.
    declaration: [WHERE, Subelement, subelement]
        WHERE: menu, fastkey, starter
        if menu: first element like: file, help, edit etc. Second like "Ctrl+p" etc.
        elif starter: sub element contains the categories if plugin has.
    '''
    actiontypes= {
        "menu":     ["file", "Ctrl+p"],
        "starter":  "activities"        # [] allowed too
    }

    ''' this file's path needed for loading gui files. FIXME as soon as possible'''
    filepath = __file__


    ''' This value is optional.
    Represent the dependencies of this plugins.
    The dependencies also plugins...
    (in tuple: name of the plugin, version of the plugin)
    '''
    dependencies = [
        #("test plugin1", 1),
        #("test plugin2", 4)
    ]


'''This value contain the reference to the plugin'''
#import plugin
#plugin = plugin.Plugin(Meta)