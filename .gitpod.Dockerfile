FROM gitpod/workspace-full
USER gitpod
RUN sudo apt update && sudo apt install ffmpeg && sudo apt clean
