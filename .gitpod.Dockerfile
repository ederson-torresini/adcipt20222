FROM gitpod/workspace-full
USER gitpod
RUN sudo apt update && sudo apt -y install ffmpeg && sudo apt clean
