document.getElementById("latestdownloadButton").addEventListener("click", function() {
    fetch("https://api.github.com/repos/JeelDobariya38/simple-calculator/releases/latest")
        .then(response => response.json())
        .then(data => {
            const assets = data.assets;
            for (const asset of assets) {
                if (asset.name.endsWith(".exe")) {
                    window.location.href = asset.browser_download_url;
                    break;
                }
            }
        })
        .catch(error => console.error("Error fetching latest release:", error));
});