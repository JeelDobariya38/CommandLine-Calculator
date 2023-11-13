document.addEventListener("DOMContentLoaded", function() {
    fetch("https://api.github.com/repos/JeelDobariya38/Simple-Calculator/releases")
        .then(response => response.json())
        .then(releases => {
            console.log(releases);
            for (var release of releases) {
                console.log(release.name);
                console.log(release.body);
                console.log(release.prerelease);
                console.log(release.published_at);
                var assets = release.assets;
                for (var asset of assets) {
                    if (asset.name.endsWith(".zip")) {
                        console.log(asset.name);
                        console.log(asset.browser_download_url);
                        break;
                    }
                }
            }
        }).catch(error => console.error("Error fetching latest release:", error));
    }
);
