---
icon: material/download
description: "Download blendOS"
hide:
  - toc
  - navigation
---

<style>
.md-typeset__table {
  width: 100%;
}

.md-typeset__table table:not([class]) {
  display: table
}

.md-content__button {
  display: none;
}

</style>

<div align="center" markdown> 
# :material-download: Download blendOS



## :simple-bittorrent: BitTorrent

[:material-file-download: Torrent](https://fosstorrents.com/thankyou/?name=blendos&cat=Latest%20Edition&id=0&hybrid=0){ .md-button target="_blank" rel="noopener noreferrer" data-umami-event="Torrent Download" } [:fontawesome-solid-magnet: Magnet](https://fosstorrents.com/distributions/blendos/#downloads){ .md-button rel="noopener noreferrer" target="_blank" data-umami-event="Magnet Download" }

<small>:fontawesome-solid-info:{ title="Info" } A webseed-capable client is **highly recommended**. A torrent client must be installed to open magnet links.</small>
{ .info }

## :material-lock: HTTPS

</div>

!!! info "Versions"
    To tell which mirrors are up-to-date, check which mirrors have the latest version <span id="v" class="noJs"></span>. All mirrors with the same version are up-to-date. If you don't see a version, something is wrong. Mirrors with an :x:{title=""} have not updated to the new version system.

    <noscript>**Since you have Javascript disabled, you will need to check manually by clicking the `Version` link under each download button.**</noscript>

<script>
var xhr6 = new XMLHttpRequest();
var fileUrl6 = 'https://git.blendos.co/api/v4/projects/32/jobs/artifacts/main/raw/version?job=build-job';
xhr6.open('GET', fileUrl6, true);
xhr6.onreadystatechange = function() {
  if (xhr6.readyState === XMLHttpRequest.DONE) {
    if (xhr6.status >= 200 && xhr6.status < 300) {
      var fileContent6 = xhr6.responseText;
      var numCharacters6 = 8; // Change this number as needed
      var firstCharacters6 = fileContent6.slice(0, numCharacters6);
      document.getElementById('v').innerHTML = "<b>(<a href='https://git.blendos.co/api/v4/projects/32/jobs/artifacts/main/raw/version?job=build-job' target='_blank' rel='noopener noreferrer'><code>" + firstCharacters6 + "</code></a>)</b>";
    } else {
      console.error('Failed to load file:', xhr6.statusText);
    }
  }
};
xhr6.onerror = function() {
  console.error('Network error occurred');
};
xhr6.send();
</script>

--8<-- "docs/download/mirrors.md"
