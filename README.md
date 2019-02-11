# Touch Me Not


## Inspiration

This project is inspired by people that are ashamed by their mental health issue and fail to get the help they need. And with today's technology where human facial features and expressions can be extracted, detected, and recognized through computer algorithms, examining a person's face can be one method of effectively discerning their genuine mood and reactions, therefore help the counselor, doctor, or teacher better assess someone's mental states using their facial expressions.

## What it does
This website assists all kinds of professionals at works in the public health sector that deals with people with mental health issues like doctors, teachers, and counselors. It detects emotional expression from the person and provides information about the person like whether if the person is under stress. This website accepts videos and breaks it down by frames. It then uses google cloud vision API to detect facial expressions of the person and generates a large data set representing a person's mood over time. The data set is then analyzed and visualized in a graph to shows the person's mental states and changes in mood over time.

## How we built it
We first make a website using JavaScript that accepts videos in mp4 and breaks it down by frames, forming an array of images using open cv. The images are then analyzed through the Vision API from Google Cloud Platform that detects facial expressions of the person and generates a 2D list representing a person's different emotion in scale. Finally, we visualize the data using matplotlib and numpy which is push back to the website.

## Tech-stack
Using Google Cloud Platform, Python, Vision API, HTML, CSS, JavaScript, JQuery and OpenCV.

## Challenges we ran into
Getting a snapshot of different scenes in a video was a difficult part. Everyone in the team was new to the Google Cloud services and the platform.

## Accomplishments that we're proud of
We were able to implement image analysis with Google Vision API - a world-leading technology - and utilized a wide spectrum of developing tools.

## What we learned
Building with a team, and tackling social issues that will affects many people in the society.

## What's next for Touch-me-not
We would integrate real-time analysis of a person's emotion without having to upload files.
