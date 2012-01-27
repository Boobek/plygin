'''
Load plugins
'''
from importlib import import_module
import logging
log = logging.getLogger("plygin-pluginloader")
logging.level = logging.DEBUG


activePlugins = [
	"example",
]

plugins = {}
__depwait = []

def __importPlugin(pluginDir):
    plugin = import_module("." + pluginDir, "languageteacher.plugins")
    log.debug("Plugin '%s' loading..", plugin.Meta.name)
    return plugin

def __depCheck(plugin):
    depsOk = True
    for deps in plugin.Meta.dependencies:
        if deps[0] not in plugins:
            depsOk = False
            if plugin not in __depwait:
                __depwait.append( plugin )
            log.debug("Plugin '%s' depending on '%s' and it's not loaded yet.",
                    plugin.Meta.name, deps[0])
    return depsOk

def __loadPlugin(plugin):
    name = plugin.Meta.name
    plugins[name] = plugin.plugin


def loadPlugins():
    log.debug("Loading plugins")
    for pluginDir in activePlugins:
        plugin = __importPlugin(pluginDir)
        if __depCheck(plugin):
            __loadPlugin(plugin)
    log.debug("Try to solve dependencies")
    while len(__depwait) > 0:
        loadedPlugin = None
        for plugin in __depwait:
            if __depCheck(plugin):
                __loadPlugin(plugin)
                loadedPlugin = plugin
                break
        __depwait.remove(loadedPlugin)

        if loadedPlugin == None: break

    if len(__depwait) > 0:
        raise RuntimeError("Unsatisfied dependencies..")
    log.debug( "Plugins loaded." )


if __name__ == "__main__":
	loadPlugins()

