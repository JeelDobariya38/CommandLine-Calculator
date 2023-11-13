/* <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/2.0.3/marked.min.js"></script> */

document.addEventListener("DOMContentLoaded", function () {
    // Ensure marked.js is loaded
    if (typeof marked === 'undefined') {
        console.error("marked.js is not loaded");
        return;
    }

    fetch("https://api.github.com/repos/JeelDobariya38/Simple-Calculator/releases")
        .then(response => response.json())
        .then(releases => {
            console.log(releases);

            // Find the "Other Releases" container
            const otherReleasesContainer = document.querySelector('.other-version');
            console.log(otherReleasesContainer)

            for (var release of releases) {
                if (!release.draft) {
                    const convertedBody = marked(release.body);
                    const releaseElement = document.createElement('div');
                    releaseElement.classList.add('release');
                    releaseElement.innerHTML = `
                        <h1>${release.name}</h1>
                        <div class="info">
                            <div><b>Prerelease: <span class="prerelease">${release.prerelease}</span></b></div>
                            <div><b>Published At: <span class="published-at">${release.published_at}</span></b></div>
                        </div>
                        <p>${convertedBody}</p>
                        <a href="${release.html_url}" target="_blank"><button>Download</button></a>
                    `;
                    otherReleasesContainer.appendChild(releaseElement);
                }
            }

            // Check if there are no other releases and display an error message
            if (otherReleasesContainer.children.length === 0) {
                const errorMsg = document.querySelector('.other-version .error-msg');
                errorMsg.style.display = 'block';
            }
        })
        .catch(error => console.error("Error fetching latest release:", error));
});
