document.getElementById("latestdownloadButton").addEventListener("click", function() {
    fetch("https://api.github.com/repos/JeelDobariya38/Simple-Calculator/releases/latest")
        .then(response => response.json())
        .then(data => {
            const assets = data.assets;
            if (assets == undefined) {
                if (data.message) {
                    console.log("latest release not found!");
                    var element = document.getElementsByClassName("error-msg")[0];
                    element.style.display = "block";
                }
            }
            else {
                for (var asset of assets) {
                    if (asset.name.endsWith(".zip")) {
                        window.location.href = asset.browser_download_url;
                        break;
                    }
                }
            }
        }).catch(error => console.error("Error fetching latest release:", error));
    }
);
