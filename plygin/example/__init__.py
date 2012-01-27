from .. import meta
class Meta(meta.Meta):
    name = "example-plugin"
    version = 1
    visibleName = "Working with example plugin"
    description = ''' This plugin is an example for  further works... '''
    actiontypes= {
        "menu":     ["file", "Ctrl+p"],
        "starter":  "activities"        # [] allowed too
    }
    filepath = __file__
    dependencies = [
        ("starter-gui-plugin", 1)
    ]


import plugin
plugin = plugin.Plugin(Meta)