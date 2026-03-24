const audioFileInput = document.getElementById("audioFile");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const statusBox = document.getElementById("status");
const transcriptBox = document.getElementById("transcript");

let isRecording = false;

audioFileInput.addEventListener("change", async () => {
    const file = audioFileInput.files[0];

    if (!file) {
        statusBox.textContent = "Idle. Waiting for input.";
        transcriptBox.value = "";
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    statusBox.textContent = "Processing audio...";
    transcriptBox.value = "";
    audioFileInput.disabled = true;

    try {
        const response = await fetch("http://127.0.0.1:8000/transcribe", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("The server could not transcribe this audio file.");
        }

        const data = await response.json();

        if (data.success) {
            transcriptBox.classList.remove("fade-in");
            void transcriptBox.offsetWidth;
            transcriptBox.classList.add("fade-in");
            statusBox.textContent = "✅ Transcription successful";
            transcriptBox.value = data.text;
        } else {
            throw new Error("Transcription failed");
        }
    } catch (error) {
        statusBox.textContent = "Unable to process audio.";
        transcriptBox.value = `Error: ${error.message || "Please check that the backend is running and try again."}`;
    } finally {
        audioFileInput.disabled = false;
    }
});

startBtn.addEventListener("click", () => {
    if (isRecording) {
        return;
    }

    isRecording = true;
    startBtn.disabled = true;
    stopBtn.disabled = false;
    statusBox.textContent = "Recording started... speak into your microphone.";
    transcriptBox.value = "Mock transcription in progress...";
});

stopBtn.addEventListener("click", () => {
    if (!isRecording) {
        return;
    }

    isRecording = false;
    startBtn.disabled = false;
    stopBtn.disabled = true;
    statusBox.textContent = "Recording stopped.";
    transcriptBox.value = "Mock transcription: this is where the recorded speech text will appear after backend integration.";
});
