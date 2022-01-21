#############
# Download videos using youtub-dl
# Author: Jonathon Lillie
# Requirements: youtube-dl.exe downloaded to the downloads folder
#############

# get the URL for the video
# the code works as well. 
# ex: https://www.youtube.com/watch?v=bvWRMAU6V-c
# or 
# bvWRMAU6V-c
$url = Read-Host -Prompt "Enter video URL:"

# Gets current users username
$username = $env:USERNAME

# Set's the command lines location to your downloads folder (where youtub-dl should be downloaded to)
Set-Location -Path C:\Users\$username\Downloads\

# runs youtube-dl with the URL you entered earlier. 
.\youtube-dl.exe $url