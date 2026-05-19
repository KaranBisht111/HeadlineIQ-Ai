const API_URL = window.location.origin;

let selectedStyle = "professional";

const textInput =
document.getElementById("textInput");

const charCount =
document.getElementById("charCount");


textInput.addEventListener("input", () => {

    charCount.innerText =
    textInput.value.length + " Characters";
});


document.querySelectorAll(".mode-btn")
.forEach(button => {

    button.addEventListener("click", () => {

        document
        .querySelectorAll(".mode-btn")
        .forEach(btn => {

            btn.classList.remove("active");
        });

        button.classList.add("active");

        selectedStyle =
        button.dataset.style;
    });
});


document
.getElementById("generateBtn")
.addEventListener(
    "click",
    generateHeadlines
);


async function generateHeadlines(){

    const text =
    textInput.value.trim();

    if(text.length < 50){

        alert(
            "Please enter at least 50 characters"
        );

        return;
    }

    const button =
    document.getElementById("generateBtn");

    try{

        button.innerText =
        "Generating...";

        button.disabled = true;

        const response = await fetch(

            `${API_URL}/generate`,

            {
                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({

                    text:text,

                    style:selectedStyle,

                    total:6
                })
            }
        );

        const result =
        await response.json();

        console.log(result);

        if(!result.success){

            alert(
                result.error ||
                result.message ||
                "Generation failed"
            );

            button.innerText =
            "Generate Headlines";

            button.disabled = false;

            return;
        }

        if(
            !result.data ||
            !result.data.analytics ||
            !result.data.headlines
        ){

            alert(
                "Invalid backend response"
            );

            console.log(result);

            button.innerText =
            "Generate Headlines";

            button.disabled = false;

            return;
        }

        renderAnalytics(
            result.data.analytics
        );

        renderHeadlines(
            result.data.headlines
        );

        button.innerText =
        "Generate Headlines";

        button.disabled = false;

    }catch(error){

        console.log(
            "Frontend Error:",
            error
        );

        alert(
            "Backend connection failed"
        );

        button.innerText =
        "Generate Headlines";

        button.disabled = false;
    }
}


function renderAnalytics(data){

    const panel =
    document.getElementById(
        "analyticsPanel"
    );

    panel.innerHTML = `

        <div class="analytics-card">

            <h4>Sentiment</h4>

            <p>
                ${data.sentiment || "N/A"}
            </p>

        </div>

        <div class="analytics-card">

            <h4>SEO Score</h4>

            <p>
                ${data.seo_score || 0}%
            </p>

        </div>

        <div class="analytics-card">

            <h4>Headline Score</h4>

            <p>
                ${data.headline_score || 0}%
            </p>

        </div>

        <div class="analytics-card">

            <h4>Readability</h4>

            <p>
                ${data.readability || "Unknown"}
            </p>

        </div>

    `;
}


function renderHeadlines(headlines){

    const section =
    document.getElementById(
        "resultsSection"
    );

    section.innerHTML = "";

    headlines.forEach(item => {

        section.innerHTML += `

            <div class="headline-card">

                <h3>${item}</h3>

                <button
                    class="copy-btn"
                    onclick="copyHeadline(\`${item}\`)"
                >
                    Copy
                </button>

            </div>
        `;
    });
}


function copyHeadline(text){

    navigator.clipboard
    .writeText(text);

    alert(
        "Headline copied successfully"
    );
}