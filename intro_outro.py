from moviepy.editor import *

# Create a list of the input videos.
input_videos = ["./raw-video/video1.mp4", "./raw-video/video2.mp4", "./raw-video/video3.mp4", "./raw-video/video4.mp4"]

print(input_videos)

# Create a list of the output videos.
output_videos = ["output1.mp4", "output2.mp4", "output3.mp4", "output4.mp4"]

# For each input video, add the intro and outro videos, and write the output video to a file.
for input_video, output_video in zip(input_videos, output_videos):
  
    input_video = VideoFileClip(input_video).fx(vfx.resize, width=1920)
    #Get the intro and outro videos.
    intro_video = VideoFileClip("./intro-outro/introvideo.mp4").fx(vfx.resize, width=1920)
    outro_video = VideoFileClip("./intro-outro/outro-video.mp4").fx(vfx.resize, width=1920)

    #Add the intro and outro videos to the input video.
    output_clip = concatenate_videoclips([intro_video, input_video, outro_video], method="compose")

    # with mpy.concatenate_videoclips([intro_video, input_video, outro_video]) as output_clip:
     #Write the output video to a file.
    output_clip.write_videofile(output_video, fps=30, codec="libx264")