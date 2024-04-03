def define_env(env):
    
    @env.macro
    def aur(package):
        return f'<a href="https://aur.archlinux.org/packages/{package}" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>AUR</sup></small></a>'
    
    @env.macro
    def archpkg(package):
        return f'<a href="https://archlinux.org/packages/?name={package}" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>:material-arch:</sup></small></a>'
    
    @env.macro
    def ubpkg(package):
        return f'<a href="https://packages.ubuntu.com/search?keywords={package}&searchon=names&suite=jammy&section=all" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>:material-ubuntu:</sup></small></a>'
    
    @env.macro
    def debpkg(package):
        return f'<a href="https://packages.debian.org/search?keywords={package}&searchon=names&suite=trixie&section=all" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>:material-debian:</sup></small></a>'
    
    @env.macro
    def fedorapkg(package):
        return f'<a href="https://packages.fedoraproject.org/search?query={package}&releases=Fedora+39&start=0" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>:material-fedora:</sup></small></a>'

    @env.macro
    def track(file):
        return f'<a href="https://github.com/blend-os/tracks/raw/main/{file}.yaml" rel="noopener noreferrer" target="_blank"><code>{file}</code></a>'
    
    @env.macro
    def custom_track(impl, file):
        return f'<a href="{impl}/{file}.yaml" rel="noopener noreferrer" target="_blank"><code>{file}</code></a>'
    
    @env.macro
    def reference(type, ref):
        return f'<a href="/reference/{type}/{ref}"><code>{ref}</code></a>'
    @env.macro
    def inlinealert(color, icon, title, text):
        return '<span class=' + color +'>**' + icon + '{ title=' + title + ' } ' + text + '**</span>'