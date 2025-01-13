# %%
import whisper  # type: ignore

model = whisper.load_model("turbo")
result = model.transcribe("input.mp4")
print(result["text"])

# %%
with open("unformatted.txt", "w") as f:
    f.write(result["text"])
# %%
