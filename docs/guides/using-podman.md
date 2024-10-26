---
icon: octicons/container-16 # Your icon, see https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/
description: "How to run Podman containers on blendOS"
---

<!-- The top-level header *must* look like this (uses the same icon defined in the frontmatter)-->

# :octicons-container-16: Using Podman

By ![Ast3risk-ops](https://github.com/Ast3risk-ops.png){ width=30 .circle } [@Ast3risk-ops](https://asterisk.lol){ target="_blank" rel="noopener" }

<!-- you can also paste a gitlab.com, blendOS gitlab, bitbucket or 𝕏 profile link here, or make a Markdown link of this format:

[@Your_Username](link-to-site-or-profile)

The image can also be a local one, store it in docs/assets/img/guides

![Your Profile Picture](../assets/img/guides/your_picture.png)

-->

!!! note "This guide is written for more experienced Linux users."

In order to run other containers (like servers) on blendOS, you must first understand that you **cannot use Docker** as it will cause conflicts. blendOS already has a different container runtime on the system, *Podman*.

Podman is like Docker, but fast, light, rootless, and small. It's 100% compatible with the Docker API and CLI syntax. It really is as simple as this:

Let's say I want to run a docker container for `nginx`. Instead of using `docker`:

```sh
docker run --name some-nginx -v /some/content:/usr/share/nginx/html:ro -d -p 8080:80 nginx
```

I can use Podman:

```sh
podman run --name some-nginx -v /some/content:/usr/share/nginx/html:ro -d -p 8080:80 docker.io/nginx
```

!!! info "Docker Hub Prefixes"
    You will notice I prefix images with `docker.io/` under Podman. This is because Podman does not use "default" registries. 
    
    All images from Docker Hub must be used as **`docker.io/image`** (for official/sponsored images) or **`docker.io/author/image`**. All other registries work as usual.

You can install {{ archpkg("podman-docker") }} to the host or make a shell alias to make this even easier.

For `docker-compose` files, just change the `#!yaml image:` section to be prefixed with `docker.io` if the image is remote and on Docker Hub. Then, just use `podman compose` instead of `docker compose`.

## Apps that use Docker

For apps like [`lazydocker`](https://github.com/jesseduffield/lazydocker){ target="_blank" rel="noopener noreferrer" } that don't support Podman directly, you will need to change your `#!sh $DOCKER_HOST` variable. First, check what it's already set to:

```sh
echo $DOCKER_HOST
```

If it points to a file called `podman.sock` anywhere, you're fine, just start the user service and socket (shown below).

If not (or if it's empty), change its value to the Podman user socket path, find this with `systemctl status --user podman.socket`.

Edit your `.bashrc` (or whatever your shell config is) and add the following:

```sh title=".bashrc"
export DOCKER_HOST="unix://<socket path>"
```

Example:

```sh title=".bashrc"
export DOCKER_HOST="unix:///run/user/1000/podman/podman.sock"
```

Instead of `docker.service` and `docker.socket`, you will have `podman.service` and `podman.socket` for rooted containers (not recommended unless rootless fails), as well as the ***user services (`systemctl --user`)*** of `podman.service` and `podman.socket` (only these two user services must be started).

```yaml title="system.yaml"
user-services:
  - 'podman'
  - 'podman.socket'
```
