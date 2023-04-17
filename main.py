from upload import uploadVideo

session_id = "1470e75460892cb15e9ad1c264ec584f"
file = "videos/test.mp4"
title = "test"
tags = ["Funny", "Joke", "fyp"]
schedule_time = 0

# Publish the video
uploadVideo(session_id, file, title, tags, verbose=True)
# Schedule the video
# uploadVideo(session_id, file, title, tags, schedule_time, verbose=True)