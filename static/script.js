async function checkPassword() {
    const password = document.getElementById('password').value;

    const response = await fetch('/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password })
    });

    const data = await response.json();

    const bar = document.getElementById('bar');
    const text = document.getElementById('strength-text');
    const feedback = document.getElementById('feedback');
    const entropy = document.getElementById('entropy');

    // Strength bar
    let width = data.score * 20;
    bar.style.width = width + "%";

    if (data.score <= 2) {
        bar.style.background = "red";
        text.textContent = "Weak";
    } else if (data.score <= 4) {
        bar.style.background = "orange";
        text.textContent = "Medium";
    } else {
        bar.style.background = "green";
        text.textContent = "Strong";
    }

    // Feedback
    feedback.innerHTML = "";
    data.feedback.forEach(item => {
        let li = document.createElement("li");
        li.textContent = item;
        feedback.appendChild(li);
    });

    // Entropy
    entropy.textContent = "Entropy: " + data.entropy;
}