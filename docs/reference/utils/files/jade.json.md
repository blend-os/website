```json title="jade.json"

{
    "partition": {
        "device": "/dev/randomdisk",
        "mode": "Manual",
        "efi": true,
        "partitions": [
            "System:/dev/randomdisk1:ext4",
            "Boot:/dev/randomdisk2:fat32"
        ]
    },
    "bootloader": {
        "type": "grub-efi",
        "location": "/boot/efi"
    },
    "locale": {
        "locale": [
            "en_US.UTF-8 UTF-8"
        ],
        "keymap": "us",
        "timezone": "GMT"
    },
    "networking": {
        "hostname": "blend",
        "ipv6": false
    },
    "users": [
        {
            "name": "user",
            "password": "SOME_PLAINTEXT_PASSWORD",
            "shell": "bash"
        }
    ],
    "flatpak": true,
    "kernel": "linux"
}

```