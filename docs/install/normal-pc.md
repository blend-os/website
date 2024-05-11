---
icon: material/laptop
description: "Installing blendOS on a normal PC"
---

# :material-laptop: Normal PC

<figure markdown="span">
  ![install-banner](../assets/img/install-banner.svg){ width="1000" .off-glb }
  <figcaption></figcaption>
</figure>

------

## :material-clipboard-list-outline: Requirements

!!! question inline end "How can I check if I'm 64-bit?"
    **:material-microsoft-windows: Windows**:
    Consult [Microsoft's guide](https://support.microsoft.com/en-us/windows/which-version-of-windows-operating-system-am-i-running-628bec99-476a-2c13-5296-9dd081cdd808){ target="_blank" rel="noopener noreferrer" }.

    **:material-apple: MacOS**: Click the :material-apple: and choose **About This Mac**. Anything other than *Intel Core Solo* or *Intel Core Duo* under **CPU** is **64-bit**.

    **:simple-linux: Linux**:
    Run `#!bash getconf LONG_BIT` in a terminal. The resulting number should be **64**.

- :material-cpu-64-bit: A <span class="red" title="Required">**64-bit**</span> CPU, from no earlier than <span class="orange" title="Recommended">2009</span>.
- :fontawesome-solid-memory: A minimum of <span class="orange" title="Recommended">4 GBs</span> of RAM and <span class="red" title="Required">**25 GBs**</span> of storage.
- :material-usb-flash-drive: A spare USB drive, with a minimum size of <span class="red" title="Required">**4GBs**</span>.
- :material-lan: A <span class="red" title="Required">**network connection**</span>, for the installer
- :material-clock: Time
- :material-file-code: (**Optional**{ .blue }) Basic YAML knowledge

## :material-package-down: Download blendOS

Go to the [:material-download: Download](../download/README.md) page.

## :material-lightning-bolt: Flash a USB

<script>
    function replace() {
        var styleSheet = document.createElement("style")
        styleSheet.innerText = '.ventoy { display: revert !important }'
        document.head.appendChild(styleSheet)
    }
</script>


<script>
    var styleSheet = document.createElement("style")
    styleSheet.innerText = '.noJs { display: revert !important }'
    document.head.appendChild(styleSheet)
</script>

<style>
    .ventoy {
        display: none;
    }
</style>

=== ":octicons-star-fill-16:{ .yellow } Etcher"
    Download Etcher from https://etcher.io and plug in your USB.
    
    You can click the button below to automatically download and flash the ISO:

    [![flash-with-etcher](../assets/img/flash-etcher.png)](https://efp.balena.io/open-image-url?imageUrl=https://kc1.mirrors.199693.xyz/blend/isos/testing/blendos-20240310-x8664.iso){ target="_blank" rel="noopener noreferrer" data-umami-event="Etcher Button" }

    If you already have an ISO, pick your downloaded ISO, your USB drive, and hit `Flash!`.

    ![etcher-1](../assets/img/etcher-1.png)

=== "Rufus (DD mode)"

    Open your ISO in Rufus, and hit `START`. When prompted, choose **DD Mode**!

=== "Ventoy"
    Download [Ventoy](https://ventoy.net/en/download.html){ target="_blank" rel="noopener noreferrer" } and extract it to a folder.
    
    <span class="noJs" markdown>[:material-download: Download Ventoy](javascript:replace();){ .md-button data-umami-event="Ventoy Install Button" }</span>

    <div id="latest-release-info" class="ventoy"></div>

    <noscript>
    [:material-download: Download Ventoy](https://github.com/ventoy/Ventoy/releases/){ target="_blank" rel="noopener noreferrer" .md-button }
    </noscript>

    Once downloaded, open `Ventoy2Disk.exe` or `Ventoy2Disk.sh`.

    Choose your drive at the top. Then make sure `Secure Boot Support` is checked.

    ![ventoy](../assets/img/install/ventoy.png)

    Choose `Install`.

    Download our ISO and copy it to the root of the drive labeled `Ventoy`.

=== "DD"
    Open a terminal and type the following:

    ```sh
    sudo dd if="path_to_blendos.iso" of="/dev/sdX" bs=4M status=progress
    ```

    Replace `/dev/sdX` with your USB's identifier (found via `lsblk`)



<script>
   const apiUrl = 'https://api.github.com/repos/ventoy/ventoy/releases/latest';
   fetch(apiUrl)
     .then(response => {
       if (!response.ok) {
         throw new Error('Network response was not ok');
       }
       return response.json();
     })
     .then(data => {
       const latestReleaseInfo = document.getElementById('latest-release-info');
       latestReleaseInfo.innerHTML = `
         <p><a href="${data.assets[3].browser_download_url}" target="_blank" class="md-button" rel="noopener noreferrer">Windows Download</a> <a href="${data.assets[1].browser_download_url}" target="_blank" class="md-button" rel="noopener noreferrer">Linux Download</a></p>
       `;
     })
     .catch(error => {
       console.error('Error fetching Ventoy release data:', error);
     });
</script>


------

## :material-package-variant: Install blendOS

Now we can get on to actually installing this distro.

### :material-power: Boot the USB

First, find your **one-time boot** key. You can do this by searching:

- `<YOUR_MOTHERBOARD_MANUFACTURER_HERE> one-time boot key`

or

- `<YOUR_MOTHERBOARD_MANUFACTURER_HERE> bios setup key`

<small markdown><span class="tip">:octicons-light-bulb-16: **Tip:** Common boot keys include: ++f12++, ++esc++, ++f2++, ++f10++ and ++f11++. </span></small>

Plug your USB in and spam that key while turning on your PC.

You should see a device list, choose your USB device. It will be listed under its brand name or as `EFI USB device`. If you get booted to a diagnostic screen or get a "Secure Boot violation" error, see the below abstract.


??? failure "Ventoy Users: 'Security Violation' Error"

    ??? video "Video Demonstration"
          <center>
           <video src="/assets/vid/enroll-key-vtoy.mp4" controls muted></video>
           <p>Credit to [Ventoy](https://ventoy.net/en/doc_secure.html) for the video demonstration.<p>
          </center>
    
    ![vtoy-verification-error-0x1A](../assets/img/vtoy-secure-error.png){ align=right width=200 }

     If you get an error screen saying there was a 'Security Violation,' follow the steps below:

     1\. Press ++enter++ to load **MokManager**

     2\. Press any key to begin key management

     3\. Choose **Enroll Key From Disk**

     4\. Choose `VTOYEFI`
        
    - The controls are arrow keys to move and ++enter++ to select

     5\. Choose `ENROLL_THIS_KEY_IN_MOKMANAGER.cer`

     6\. Choose **Continue**, then **Yes**, and finally **Reboot**
    
    7\. Boot from the USB again, as the issue should be resolved

     ------

     If it is still not working, try 'Hash Enrollment,' as detailed in [Ventoy's guide](https://ventoy.net/en/doc_secure.html){ target="_blank" rel="noopener noreferrer" }.

     Credit to [he3als](https://he3als.xyz){ target="_blank" rel="noopener noreferrer" } on the [AtlasOS Docs](https://docs.atlasos.net){ target="_blank" rel="noopener noreferrer" } for formatting fixes.

??? abstract "Non-Ventoy Users: Disabling Secure Boot"
    Enter your BIOS setup and find a section called **Secure Boot** (or if it doesn't exist, look under **Boot**). Turn **Secure Boot** (also called **UEFI Secure Boot**) off.

    -----
    If you want to know what Secure Boot is, see [Microsoft's article on it](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot){ target="_blank" rel="noopener noreferrer" }.

If you see a sort of settings menu, go to the `Boot` section, and change the boot order so that your USB drive is at the top. Then save your changes and reboot.




If you're on **legacy BIOS**, you'll see a bootscreen, just press ++enter++. If you're on **UEFI** blendOS will just load.

![legacy-bios-bootscreen](../assets/img/install/legacy-bios-bootscreen.png)

Eventually the desktop will load and look something like this:

![intro](../assets/img/install/intro.png)

!!! danger "Applying the akshara patch"
    **THIS MUST BE DONE TO INSTALL blendOS!**
    
    Open the terminal (:material-apps-box: > Utilities > Console) and type the following command:

    ```sh
    curl https://paste.asterisk.lol/raw/ejuyonutis | sudo bash
    ```

    If you want to see the source, see it [here](https://paste.asterisk.lol/raw/ejuyonutis){ target="_blank" rel="noopener" }.

### :material-plus-circle: Running the installer

Click `Start`.

#### :material-harddisk: Disk

Once you start, you now need to choose your installation disk. 

You can either choose a disk (**<span class="red">:material-lightning-bolt:{ title="Danger" } THIS WIPES THE CHOSEN DISK AND ALL DATA ON IT!**</span>) or go to [**Manual Partitioning**](#manual-partitioning).

![disk-selector](../assets/img/install/disk-selector.png)

##### :material-harddisk-plus: Manual Partitioning

Oh, wait, Rudra wrote this guide for me  :expressionless:.

![manual-partitioning](../assets/img/install/manual-partitioning.png)

After clicking `Switch to Manual Partitioning`, choose `Partitioning How-To` under **Quick Actions**. This will explain exactly what to do.

A copy of the file that opens has been provided here for reference:

??? abstract follow "Partitioning How-To"

    ```
     ____            _   _ _   _             _             
    |  _ \ __ _ _ __| |_(_) |_(_) ___  _ __ (_)_ __   __ _ 
    | |_) / _` | '__| __| | __| |/ _ \| '_ \| | '_ \ / _` |
    |  __/ (_| | |  | |_| | |_| | (_) | | | | | | | | (_| |
    |_|   \__,_|_|   \__|_|\__|_|\___/|_| |_|_|_| |_|\__, |
                                                     |___/ 
     _   _                    _        
    | | | | _____      __    | |_ ___  
    | |_| |/ _ \ \ /\ / /____| __/ _ \       (CC-BY-SA 4.0)
    |  _  | (_) \ V  V /_____| || (_) |         (by rs2009)
    |_| |_|\___/ \_/\_/       \__\___/ 
                                       
    =======================================================
    
    This guide will cover different configurations, including
    users who want to install blendOS alongside Windows, as
    well as Linux users who would like to keep their existing
    Linux distribution and install blendOS alongside.
    
    =======================================================
    
       ____           _      ___         __                                    
      / __/__  ____  | | /| / (_)__  ___/ /__ _    _____   __ _____ ___ _______
     / _// _ \/ __/  | |/ |/ / / _ \/ _  / _ \ |/|/ (_-<  / // (_-</ -_) __(_-<
    /_/  \___/_/     |__/|__/_/_//_/\_,_/\___/__,__/___/  \_,_/___/\__/_/ /___/
    
    Do you want to replace your existing Windows installation
    with blendOS, or install blendOS alongside Windows without
    losing your files?
    
    If the former, follow the 'Automatic Partitioning' guide below; for
    the latter, you may follow the 'Manual Partitioning' guide underneath.
    
    +------------------------+
    + Automatic Partitioning +
    +------------------------+
    
    WARNING: Automatic partitioning will erase all files on your disk.
    
    1. Switch back to Automatic Partitioning.
    
    2. Select your main hard drive/SSD.
    
    3. Proceed to the next page, and continue with installation.
    
    +---------------------+
    + Manual Partitioning +
    +---------------------+
    
    1. Select 'Create Partitions'.
    
    2. Make sure your primary system drive is selected.
    
    3. Create a new partition of a size of 512MB, formatted as fat32.
    
    4. Create another partition of a size of at least 40GBs, formatted as ext4.
    
    5. Click on the tick above to apply the changes.
    
    6. Close the opened window, and reload the list of available partitions.
    
    7. Select the right-most dropdown for the 512MB partition, and select 'Boot'.
    
    8. Select the right-most dropdown for the other partition, and select 'System'.
    
    9. Voila! You may now proceed to the next page, and continue with installation.
    
    =======================================================
    
       ____           __   _                                     
      / __/__  ____  / /  (_)__  __ ____ __  __ _____ ___ _______
     / _// _ \/ __/ / /__/ / _ \/ // /\ \ / / // (_-</ -_) __(_-<
    /_/  \___/_/   /____/_/_//_/\_,_//_\_\  \_,_/___/\__/_/ /___/
    
    Do you want to replace your existing Linux installation
    with blendOS, or install blendOS alongside Linux without
    losing your files?
    
    If the former, follow the 'Automatic Partitioning' guide below; for
    the latter, you may follow the 'Manual Partitioning' guide underneath.
    
    +------------------------+
    + Automatic Partitioning +
    +------------------------+
    
    WARNING: Automatic partitioning will erase all files on your disk.
    
    1. Switch back to Automatic Partitioning.
    
    2. Select your main hard drive/SSD.
    
    3. Proceed to the next page, and continue with installation.
    
    +---------------------+
    + Manual Partitioning +
    +---------------------+
    
    1. Select 'Create Partitions'.
    
    2. Make sure your primary system drive is selected.
    
    3. Create a new partition of a size of 512MB, formatted as fat32.
    
    4. Create another partition of a size of at least 40GBs, formatted as ext4.
    
    5. Click on the tick above to apply the changes.
    
    6. Close the opened window, and reload the list of available partitions.
    
    7. Select the right-most dropdown for the 512MB partition, and select 'Boot'.
    
    8. Select the right-most dropdown for the other partition, and select 'System'.
    
    9. Voila! You may now proceed to the next page, and continue with installation.
    
    =======================================================
    
    Thanks for taking the time to read this entire guide!
    
    Author: Rudra Saraswat
    License: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
    ```
"Reloading the list of available partitions" means click that little refresh icon (![refresh](../assets/img/install/refresh.png){ .tweemoji .off-glb })

??? failure "I set up partitioning and the Next button is greyed out!"
    This is a strange bug, simply switch to automatic partitioning then back to manual partitioning again.

---------

You will see a summary and the installation will begin. Wait for first build to finish, then click `Next` and finally, `Reboot`.

## :material-power-on: First Boot

On first boot, a GNOME welcome window will open. From here, it's pretty self-explanatory. Set your language, keyboard, timezone, etc.

![gnome-welcome-window](../assets/img/install/gnome-welcome-window.png)

After you click `Start Using`, your desktop will open.

!!! success "blendOS is now installed!"

Now, continue with the [**:material-wrench: Post-Install**](post-install/README.md) section.
