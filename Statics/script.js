const form = document.getElementById("Predict");
const btn = document.getElementById("submitBtn");
const output = document.getElementById("output");
const soil_re = document.getElementById("soil_re");
const crop_re = document.getElementById("crop_re");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    if(btn.innerHTML === "Reset")
    {
        window.location.reload();
        return;
    }

    const data = {
        pH : document.getElementById("pH").value,
        humidity : document.getElementById("humidity").value, 
        rainfall : document.getElementById("rainfall").value,
        temperature : document.getElementById("temperature").value,
        N : document.getElementById("N").value,
        P : document.getElementById("P").value,
        K : document.getElementById("K").value
    };

    fetch("/predict_all", {
        method: "POST", 
        headers: {
            "Content-Type" : "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        if(response.soil_type && response.crop_type)
        {
            soil_re.textContent = response.soil_type;
            crop_re.textContent = response.crop_type;
            output.style.display = "block";
            btn.innerText = "Reset";
        }
        else
        {
            alert("Error" + response.error);
        }
    })
    .catch(err => {
        alert("Something went wrong");
        console.error(err);
    });
});