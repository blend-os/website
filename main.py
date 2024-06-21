#    Copyright 2024 Asterisk
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#      https://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.



def define_env(env):
    
    @env.macro
    def aur(package):
        return f'<a href="https://aur.archlinux.org/packages/{package}" title="Arch User Repository Package" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>AUR</sup></small></a>'
    
    @env.macro
    def archpkg(package):
        return f'<a href="https://archlinux.org/packages/?name={package}" title="Arch Repo Package" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>:material-arch:</sup></small></a>'
    
    @env.macro
    def ubpkg(package):
        return f'<a href="https://packages.ubuntu.com/search?keywords={package}&searchon=names&suite=jammy&section=all" title="Ubuntu 22.04 Package" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>:material-ubuntu:</sup></small></a>'
    
    @env.macro
    def debpkg(package):
        return f'<a href="https://packages.debian.org/search?keywords={package}&searchon=names&suite=trixie&section=all" title="Debian Testing Package" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>:material-debian:</sup></small></a>'
    
    @env.macro
    def fedorapkg(package):
        return f'<a href="https://packages.fedoraproject.org/search?query={package}&releases=Fedora+39&start=0" title="Fedora 39 Package" rel="noopener noreferrer" target="_blank"><code>{package}</code><small><sup>:material-fedora:</sup></small></a>'

    @env.macro
    def track(file):
        return f'<a href="https://github.com/blend-os/tracks/raw/main/{file}.yaml" title="Official Track" rel="noopener noreferrer" target="_blank"><code>{file}</code><small><sup>:material-file-code:</sup></small></a>'
    
    @env.macro
    def custom_track(impl, file):
        return f'<a href="{impl}/{file}.yaml" rel="noopener noreferrer" target="_blank" title="Unofficial Track"><code>{file}</code><small><sup>:material-file-code:</sup></small></a>'
    
    @env.macro
    def reference(type, ref):
        return f'<a href="/reference/{type}/{ref}" title="Reference Page"><code>{ref}</code></a>'
    @env.macro
    def inlinealert(color, icon, title, text):
        return '<span class=' + color +'>**' + icon + '{ title=' + title + ' } ' + text + '**</span>'
    @env.macro
    def dockerhub(author, image):
        return f'<a href="https://hub.docker.com/r/{author}/{image}" title="Docker Hub" rel="noopener noreferrer" target="_blank"><code>{author}/{image}</code><small><sup>:fontawesome-brands-docker:</sup></small></a>'
    @env.macro
    def ghcr(author, image):
        return f'<a href="https://ghcr.io/{author}/{image}" title="Github Container Registry" rel="noopener noreferrer" target="_blank"><code>{author}/{image}</code><small><sup>:octicons-container-16:</sup></small></a>'
    @env.macro
    def quay(author, image):
        return f'<a href="https://quay.io/{author}/{image}" title="Quay.io" rel="noopener noreferrer" target="_blank"><code>{author}/{image}</code><small><sup><span class="icon-link-misc">:misc-quay:</span></sup></small></a>'
    @env.macro
    def github(user, repo):
        return f'<a href="https://github.com/{user}/{repo}" title="Github Repo" rel="noopener noreferrer" target="_blank"><code>{user}/{repo}</code><small><sup>:fontawesome-brands-github:</sup></small></a>'
    @env.macro
    def gitlab(user,  repo, subgroup="", subgroup1=""):
        return f'<a href="https://gitlab.com/{user}/{subgroup}/{subgroup1}/{repo}" title="Gitlab.com Repo" rel="noopener noreferrer" target="_blank"><code>{user}/{repo}</code><small><sup>:fontawesome-brands-gitlab:</sup></small></a>'
    @env.macro
    def codeberg(user, repo):
        return f'<a href="https://codeberg.org/{user}/{repo}" title="Codeberg Repo" rel="noopener noreferrer" target="_blank"><code>{user}/{repo}</code><small><sup>:simple-codeberg:</sup></small></a>'
    @env.macro
    def blendgit(user, repo, subgroup="", subgroup1=""):
        return f'<a href="https://git.blendos.co/{user}/{subgroup}/{subgroup1}/{repo}" title="blendOS Gitlab Repo" rel="noopener noreferrer" target="_blank"><code>{user}/{repo}</code><small><sup>:distro-blend:</sup></small></a>'
    @env.macro
    def sourcehut(user, repo):
        return f'<a href="https://sr.ht/~{user}/{repo}" title="Sourcehut Repo" rel="noopener noreferrer" target="_blank"><code>~{user}/{repo}</code><small><sup>:simple-sourcehut:</sup></small></a>'