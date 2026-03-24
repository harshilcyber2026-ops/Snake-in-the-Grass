// FlagVault CTF Scripting
const CORRECT_FLAG_INNER = "py_0bfusc4t10n_d3c0d3d";

function toggleHint(id) {
    const hint = document.getElementById(id);
    hint.classList.toggle('revealed');
}

function submitFlag() {
    const input = document.getElementById('flagInput').value.trim();
    const resultDiv = document.getElementById('result');

    // Check if user entered the full flag or just the inner part
    // The prefix is already in the UI, so we check for the inner part
    if (input === CORRECT_FLAG_INNER || input === `FlagVault{${CORRECT_FLAG_INNER}}`) {
        resultDiv.textContent = "SUCCESS: Flag captured! 250 points awarded to your profile.";
        resultDiv.className = "submit-result correct";
        
        // Trigger a small effect
        console.log("%c [!] DATABASE BREACH SUCCESSFUL ", "background: #00e8c8; color: #03080c; font-weight: bold;");
    } else {
        resultDiv.textContent = "FAILURE: Incorrect flag or malformed syntax. Try again.";
        resultDiv.className = "submit-result incorrect";
    }
}
