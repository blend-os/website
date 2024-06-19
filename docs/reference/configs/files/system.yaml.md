<style>
:root {
  --md-tooltip-width: 700px;
}
</style>

```yaml title="system.yaml"
repo: 'https://pkg-repo.blendos.co' # (1)!

arch-repo: 'https://geo.mirror.pkgbuild.com' # (10)!

impl: 'https://github.com/USER/REPO/raw/BRANCH' # (2)!

track: 'plasma' # (3)!

packages: # (4)!
  - 'package_1'
  - 'package_2'

aur-packages: # (5)!
  - 'package_1-git'
  - 'package_2-bin'

services: # (6)!
  - 'service_1'

user-services: # (9)!
  - 'user-service_1'

package-repos: # (7)!
  - name: 'REPO_NAME'
    repo-url: 'REPO_URL'

commands: # (8)!
  - 'echo command_1'
  - 'echo command_2'
```

1.  :material-cog-box: **`repo`**
          
    **Type:** string

    **Default Value:** `https://pkg-repo.blendos.co`

    !!! warning "This option must be set."

    Sets the repo for the core blendOS packages.

2.  :material-cog-box: **`impl`**
    
    **Type:** string

    **Default Value:** `https://github.com/blend-os/tracks/raw/main`

    !!! warning "This option must be set."

    Sets the raw URL prefix (track files are appended to the prefix to make a URL). 
    
    This must be set to ensure that the full URL will serve all available files with a [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type){ target="_blank" rel="noopener noreferrer" } of `text/plain`.

    ??? example
        If the start of the file looks like this:
        
         ```yaml
         repo: 'https://pkg-repo.blendos.co'

         impl: 'https://github.com/blend-os/tracks/raw/main'

         track: 'plasma'
         
         ...
         ```

         The fully generated URL would be:

         ```
         https://github.com/blend-os/tracks/raw/main/plasma.yaml
         ```

         which would redirect to:

         ```
         https://raw.githubusercontent.com/blend-os/tracks/main/plasma.yaml
         ```

        which serves the file with a [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type){ target="_blank" rel="noopener noreferrer" } of `text/plain`.


3.  :material-cog-box: **`track`**
    
    **Type:** string

    !!! warning "This option must be set."

    Sets the track (a mini `system.yaml`), which must be a YAML file in the folder of the `impl` URL.

    Available options are determined by the `impl` URL.

    If you are creating a custom track that does not inherit anything, set this value to `custom`.

    ??? example
        If I have a track folder/repo with the following files:
        
        - :material-file-code: `track-1.yaml`
        - :material-file-code: `track-2.yaml`
        

        and I set my `impl` URL properly, I then have 2 track options:

        ```yaml
        track: 'track-1'
        ```

        and

        ```yaml
        track: 'track-2'
        ```

4.  :material-cog-box: **`packages`**
    
    **Type**: array

    A list of packages to install using `pacman` (includes any custom repos you have set).

5.  :material-cog-box: **`aur-packages`**
    
    **Type**: array

    A list of AUR packages to install using `paru`.

6.  :material-cog-box: **`services`**
    
    **Type:** array

    A list of services to start at boot using `systemd`.

7.  :material-cog-box: **`package-repos`**
    
    **Type:** object array

    Custom repos to add to `pacman.conf`.

    `name`: The repo's name parameter in `pacman.conf` (the value between `[]`)

    `repo-url`: The repo's URL (no mirrorlists) (the `Server` variable from `pacman.conf`)

    ??? abstract "Value Placement"
        ```ini title="pacman.conf"
        [name]
        Server = repo-url
        SigLevel = Never
        ```

    ??? example "Example: Chaotic AUR"
        To add the [Chaotic AUR](https://aur.chaotic.cx){ target="_blank" rel="noopener noreferrer" }, the values here would be set to the following:

        !!! warning "The `name` parameter is used as `$repo` in these URLs, so do not change it from the maintainer's default!"

        ```yaml
        package-repos:
          - name: 'chaotic-aur'
            repo-url: 'https://cdn-mirror.chaotic.cx/$repo/$arch'
        ```

8.  :material-cog-box: **`commands`**
    
    **Type:** array

    A list of commands to be run as `root` at system build.

9.  :material-cog-box: **`user-services`**
    
    **Type:** array

    A list of services to start at system boot at the *user* level (`systemctl --user`).

10. :material-cog-box: **`arch-repo`**
    
    **Type:** string

    **Default Value:** `https://geo.mirror.pkgbuild.com`

    !!! note "This is not specified in the file, but is rather the default if no value is specified."

    The main Arch Linux repo to use in `pacman.conf`.

    ??? warning "Do not put a trailing / at the end of the URL."
        Do not do this:

        ```yaml title="system.yaml"
        arch-repo: 'https://geo.mirror.pkgbuild.com/'
        ```

        Do this:
        
        ```yaml title="system.yaml"
        arch-repo: 'https://geo.mirror.pkgbuild.com'
        ```

    You can find a list of mirror URLs by visiting https://cloudflaremirrors.com{ target="_blank" rel="noopener noreferrer" } (and looking at the bullet list, this shows nearby mirrors) or the [Arch mirrorlist](https://archlinux.org/mirrorlist/?protocol=https&use_mirror_status=on){ target="_blank" rel="noopener noreferrer" }. Only copy the first part of the URL (before `$repo`).

    ??? example
        If I want to use the University of Waterloo's mirror (:flag_ca:):

        ```title="URL shown in the mirrorlist"
        https://mirror.csclub.uwaterloo.ca/archlinux/$repo/os/$arch
        ```

        ```yaml title="system.yaml"
        arch-repo: 'https://mirror.csclub.uwaterloo.ca/archlinux'
        ```

        You put the link to the folder that has a directory list like this:

        ```title="Some Mirror"
        .
        ├── 󰉋 core
        ├── <variants>
        ├── 󰉋 community
        ├── <variants>
        ├── 󰉋 multilib
        ├── <variants>
        └── <more folders>
        ```
