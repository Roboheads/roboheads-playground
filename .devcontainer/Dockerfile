# ROS 2 Jazzy for the RoboHeads trainings: desktop (rqt, RViz, demo nodes) + colcon
FROM osrf/ros:jazzy-desktop

RUN apt-get update \
    && apt-get install -y --no-install-recommends ros-dev-tools python3-pip git nano \
    && rm -rf /var/lib/apt/lists/*

# Week 3: Gazebo (via ros_gz) + TurtleBot3 sim and teleop
RUN apt-get update \
    && apt-get install -y --no-install-recommends ros-jazzy-turtlebot3-gazebo ros-jazzy-turtlebot3-teleop \
    && rm -rf /var/lib/apt/lists/*
# Gazebo's default ogre2 renderer segfaults on software GL (no GPU) in the virtual desktop; ogre1 works
RUN sed -i 's#<render_engine>ogre2</render_engine>#<render_engine>ogre</render_engine>#' /opt/ros/jazzy/share/turtlebot3_gazebo/worlds/*.world
