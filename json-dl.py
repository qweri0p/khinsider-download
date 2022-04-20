#!/usr/bin/env python
import sys, json, os
if __name__ == '__main__':
    # COPY + PASTE from main script
    try:
        try:
            from importlib.util import find_spec as find_module # Python 3.4+
        except ImportError:
            from importlib import find_loader as find_module # Python 3.3
    except ImportError:
        from imp import find_module # Python 2

    # User-friendly name, import name, pip specification.
    requiredModules = [
        ['requests', 'requests', 'requests >= 2.0.0, < 3.0.0'],
        ['clint', 'clint', 'clint >= 0.3.0, < 0.4.0'],
        ['Beautiful Soup 4', 'bs4', 'beautifulsoup4 >= 4.4.0, < 5.0.0']
    ]

    def moduleExists(name):
        try:
            result = find_module(name)
        except ImportError:
            return False
        else:
            return result is not None
    def neededInstalls(requiredModules=requiredModules):
        uninstalledModules = []
        for module in requiredModules:
            if not moduleExists(module[1]):
                uninstalledModules.append(module)
        return uninstalledModules

    def install(package):
        nowhere = open(os.devnull, 'w')
        exitStatus = subprocess.call([sys.executable, '-m', 'pip', 'install', package],
                                     stdout=nowhere,
                                     stderr=nowhere)
        if exitStatus != 0:
            raise OSError("Failed to install package.")
    def installModules(modules, verbose=True):
        for module in modules:
            if verbose:
                print("Installing {}...".format(module[0]))
            
            try:
                install(module[2])
            except OSError as e:
                if verbose:
                    print("Failed to install {}. "
                          "You may need to run the script as an administrator "
                          "or superuser.".format(module[0]),
                          file=sys.stderr)
                    print("You can also try to install the package manually "
                          "(pip install \"{}\")".format(module[2]),
                          file=sys.stderr)
                raise e
    def installRequiredModules(needed=None, verbose=True):
        needed = neededInstalls() if needed is None else needed
        installModules(neededInstalls(), verbose)

    needed = neededInstalls()
    if needed:
        if moduleExists('pip'):
            # Needed to call pip the official way.
            import subprocess
        else:
            print("You don't seem to have pip installed!", file=sys.stderr)
            print("Get it from https://pip.readthedocs.org/en/latest/installing.html", file=sys.stderr)
            sys.exit(1)

    try:
        installRequiredModules(needed)
    except OSError:
        sys.exit(1)


import khinsider
f = open('music.json')
def dl(ost, fmt):
    khinsider.download(ost,ost,True,[fmt],True)
    with open('downloaded.txt', 'a') as f:
        f.write(i + '\n')
try:
    data = json.load(f)
except:
    print("Your music.json isn't written correctly.")
    exit()
for i in data["mp3"]:
    dl(i, 'mp3')
print("Downloaded all mp3 soundtracks")
for i in data["flac"]:
    dl(i,"flac")
print("Downloaded all flac soundtracks")
for i in data["m4a"]:
    dl(i, 'm4a')
print("Downloaded all m4a soundtracks")
print("Done")
