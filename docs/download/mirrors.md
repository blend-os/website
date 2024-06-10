
| :material-map-marker: Location          |  :material-format-letter-case: Name  |               :material-speedometer: Bandwidth               |             :material-sitemap: CDN              |                                                                                            :material-link: URL                                                                                            |
| --------------------------------------- | :----------------------------------: | :----------------------------------------------------------: | :---------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| :flag_de:{title=""} Germany       | :simple-gitlab: Master Build Server (blendOS Gitlab) |                           Unknown                            |     :octicons-x-12:{ .red } {data-sort='0'}     |            [:material-download: Download](https://git.blendos.co/api/v4/projects/32/jobs/artifacts/main/raw/blendOS.iso?job=build-job){ target="_blank" rel="noopener noreferrer" .md-button data-umami-event="Gitlab Download" } <br><span id="firstCharacters" class="noJs mt-1"></span> <noscript>[`Version`](https://git.blendos.co/blendos/image-builder/-/commits/main){ target="_blank" rel="noopener noreferrer" }</noscript> <br><span class="info">:fontawesome-solid-info:{ title="Info" } This mirror will always be up to date.<small></small></span>            |
| :flag_us:{title=""} United States       |               Otus9051               |                  10Gbps { data-sort='10' }                   |    :octicons-x-12:{ .red } { data-sort='0' }    | [:material-download: Download](https://kc1.mirrors.199693.xyz/blend/isos/testing/blendOS.iso){ .md-button target="_blank" rel="noopener noreferrer" data-umami-event="Otus USA Download" }<br><span class="noJs mt-1" id="otus"></span> <noscript>[`Version`](https://kc1.mirrors.199693.xyz/blend/isos/testing/version){ target="_blank" rel="noopener noreferrer" }</noscript> |
| :flag_de:{title=""} Germany             |              Sahilister              |                   1Gbps { data-sort='1' }                    |    :octicons-x-12:{ .red } { data-sort='0' }    |               [:material-download: Download](https://mirrors.de.sahilister.net/blendos/){ .md-button target="_blank" data-umami-event="Sahilister Download" }<br><span class="noJs mt-1" id="sahilister"></span> <noscript>[`Version`](https://mirrors.de.sahilister.net/blendos/version){ target="_blank" rel="noopener noreferrer" }</noscript>               |
| :flag_kr:{title=""} South Korea         |              YuruMirror              |                   1Gbps { data-sort='1' }                    |    :octicons-x-12:{ .red } { data-sort='0' }    |  [:material-download: Download](https://mirror.funami.tech/blendos/blendOS.iso){ target="_blank" rel="noopener noreferrer" .md-button data-umami-event="Funami Download" } <br><span class="noJs mt-1" id="yuru"></span> <noscript>[`Version`](https://mirror.funami.tech/blendos/version){ target="_blank" rel="noopener noreferrer" }</noscript>   |
| :flag_de:{title=""} Germany             |                ico277                | :material-approximately-equal:0.5-12Gbps { data-sort='0.5' } |             :octicons-x-12:{ .red }             |      [:material-download: Download](https://mirror.ico277.xyz/blendos/testing/blendos-20240310-x8664.iso){ .md-button target="_blank" rel="noopener noreferrer" data-umami-event="ico277 Download" } <br>Version: :x:{title=""}     |
| :flag_ca:{title=""} Canada              |            AsteriskCloud             |                  0.2Gbps {data-sort='0.2'}                   |             :octicons-x-12:{ .red }             |               [:material-download: Download](https://blend.asterisk.lol/dvd/v4/blendOS.iso){ .md-button target="_blank" data-umami-event="AsteriskCloud Download" }<br><span class="noJs mt-1" id="asterisk"></span> <noscript>[`Version`](https://blend.asterisk.lol/dvd/v4/version){ target="_blank" rel="noopener noreferrer" }</noscript>                |
| :flag_nz:{title=""} New Zealand         |        TheoM's Mirror Service        | :material-approximately-equal:0.5-10Gbps { data-sort='0.5' } |    :octicons-x-12:{ .red } { data-sort='0' }    |    [:material-download: Download](https://blendos.mirrors.theom.nz/isos/testing/blendos-20240310-x8664.iso){ .md-button rel="noopener noreferrer" target="_blank" data-umami-event="TheoM Download" }  <br>Version: :x:{title=""}     |



<script>
var xhr = new XMLHttpRequest();
var fileUrl = 'https://git.blendos.co/api/v4/projects/32/jobs/artifacts/main/raw/version?job=build-job';
xhr.open('GET', fileUrl, true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    if (xhr.status >= 200 && xhr.status < 300) {
      var fileContent = xhr.responseText;
      var numCharacters = 8; // Change this number as needed
      var firstCharacters = fileContent.slice(0, numCharacters);
      document.getElementById('firstCharacters').innerHTML = "Version: <a href='https://git.blendos.co/blendOS/image-builder/-/commit/" + fileContent +  "' target='_blank' rel='noopener noreferrer'><code>" + firstCharacters + "</code></a>";
    } else {
      console.error('Failed to load file:', xhr.statusText);
    }
  }
};
xhr.onerror = function() {
  console.error('Network error occurred');
};
xhr.send();

var xhr2 = new XMLHttpRequest();
var fileUrl2 = 'https://kc1.mirrors.199693.xyz/blend/isos/testing/version';
xhr2.open('GET', fileUrl2, true);
xhr2.onreadystatechange = function() {
  if (xhr2.readyState === XMLHttpRequest.DONE) {
    if (xhr2.status >= 200 && xhr2.status < 300) {
      var fileContent2 = xhr2.responseText;
      var numCharacters2 = 8; // Change this number as needed
      var firstCharacters2 = fileContent2.slice(0, numCharacters2);
      document.getElementById('otus').innerHTML = "Version: <a href='https://kc1.mirrors.199693.xyz/blend/isos/testing/version' target='_blank' rel='noopener noreferrer'><code>" + firstCharacters2 + "</code></a>";
    } else {
      console.error('Failed to load file:', xhr2.statusText);
    }
  }
};
xhr2.onerror = function() {
  console.error('Network error occurred');
};
xhr2.send();

var xhr3 = new XMLHttpRequest();
var fileUrl3 = 'https://mirrors.de.sahilister.net/blendos/version';
xhr3.open('GET', fileUrl3, true);
xhr3.onreadystatechange = function() {
  if (xhr3.readyState === XMLHttpRequest.DONE) {
    if (xhr3.status >= 200 && xhr3.status < 300) {
      var fileContent3 = xhr3.responseText;
      var numCharacters3 = 8; // Change this number as needed
      var firstCharacters3 = fileContent3.slice(0, numCharacters3);
      document.getElementById('sahilister').innerHTML = "Version: <a href='https://mirrors.de.sahilister.net/blendos/version' target='_blank' rel='noopener noreferrer'><code>" + firstCharacters3 + "</code></a>";
    } else {
      console.error('Failed to load file:', xhr3.statusText);
    }
  }
};
xhr3.onerror = function() {
  console.error('Network error occurred');
};
xhr3.send();

var xhr4 = new XMLHttpRequest();
var fileUrl4 = 'https://mirror.funami.tech/blendos/version';
xhr4.open('GET', fileUrl4, true);
xhr4.onreadystatechange = function() {
  if (xhr4.readyState === XMLHttpRequest.DONE) {
    if (xhr4.status >= 200 && xhr4.status < 300) {
      var fileContent4 = xhr4.responseText;
      var numCharacters4 = 8; // Change this number as needed
      var firstCharacters4 = fileContent4.slice(0, numCharacters4);
      document.getElementById('yuru').innerHTML = "Version: <a href='https://mirror.funami.tech/blendos/version' target='_blank' rel='noopener noreferrer'><code>" + firstCharacters4 + "</code></a>";
    } else {
      console.error('Failed to load file:', xhr4.statusText);
    }
  }
};
xhr4.onerror = function() {
  console.error('Network error occurred');
};
xhr4.send();

var xhr5 = new XMLHttpRequest();
var fileUrl5 = 'https://blend.asterisk.lol/dvd/v4/version';
xhr5.open('GET', fileUrl5, true);
xhr5.onreadystatechange = function() {
  if (xhr5.readyState === XMLHttpRequest.DONE) {
    if (xhr5.status >= 200 && xhr5.status < 300) {
      var fileContent5 = xhr5.responseText;
      var numCharacters5 = 8; // Change this number as needed
      var firstCharacters5 = fileContent5.slice(0, numCharacters5);
      document.getElementById('asterisk').innerHTML = "Version: <a href='https://blend.asterisk.lol/dvd/v4/version' target='_blank' rel='noopener noreferrer'><code>" + firstCharacters5 + "</code></a>";
    } else {
      console.error('Failed to load file:', xhr5.statusText);
    }
  }
};
xhr5.onerror = function() {
  console.error('Network error occurred');
};
xhr5.send();
</script>

<script>
    var styleSheet = document.createElement("style")
    styleSheet.innerText = '.noJs { display: revert !important }'
    document.head.appendChild(styleSheet)
</script>