import os

# Exactly two sentences; exactly 140 UTF-8 characters.
STORY = "I checked the security camera to see who rang the bell at 3 a.m. The footage showed me opening the door, smiling at someone I could not see."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(STORY)

with open("/output/entry.txt", "rb") as f:
    data = f.read()
print("byte count:", len(data))
print("byte-identical:", data == STORY.encode("utf-8"))
