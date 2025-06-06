
import json

# Load the full channel stats JSON
with open('top_youtube_channels_stats.json', 'r') as f:
    full_data = json.load(f)

# Slice the top 100
top_100 = full_data[:100]

# Save to a new JSON file
with open('top_100_youtube_channels.json', 'w') as f:
    json.dump(top_100, f, indent=2)

print("✅ top_100_youtube_channels.json generated.")
