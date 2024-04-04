<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3002B_Intelligent_Robotics_Implementation/blob/main/Misc/Logos/Logotipo%20Vertical%20Bco_Transparente.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3002B_Intelligent_Robotics_Implementation/blob/main/Misc/Logos/Logotipo%20Vertical%20Azul%20transparente.png">
  <img alt="Shows ITESM logo in black or white." width="160" align="right">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3002B_Intelligent_Robotics_Implementation/blob/main/Misc/Logos/MCR2_Logo_White.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3002B_Intelligent_Robotics_Implementation/blob/main/Misc/Logos/MCR2_Logo_Black.png">
  <img alt="Shows MCR2 logo in black or white." width="150" align="right">
</picture>

---
# TE3002B Intelligent Robotics Implementation

  ## Introduction
   * This course, developed by Manchester Robotics ltd. (MCR2), aims to provide students with understanding of modern autonomous systems.
   * This course is divided into ten sessions, carefully designed for the user to learn about the different aspects of robotics, from navigation techniques to advanced image recognition and Machine Learning implementation using the Puzzlebot and ROS.
   * This course will be based on challenges to make the student aware of the problems faced during the implementation of advanced intelligent algorithms in robotics.
   * This branch contains all the presentations, activities and files required for the “TE3002B Intelligent Robotics Implementation” course of the Tec de Monterrey.
   * This repository is organised by sessions, each subfolder contains all the neccesary files for each one of the activities of this course.

   
## General Information
* Duration: 10 Weeks
* Sessions: Thursdays  (13:00 – 15:00)
* Starts: April 1st
* Ends: June 14th
* ZOOM Link Classes: https://itesm.zoom.us/j/4779422764

## Live Sessions (Recordings)
https://drive.google.com/drive/folders/1q1FLw9df18JEB5NbzqEM48_30Une512R?usp=drive_link

## General Requirements
General requirements. Please be aware that a set of requirements especific for each session will be shown in each session subsection (Some items may be repeated).
* Computer with access to Zoom (online classes).
* Computer with Ubuntu 22.04 and ROS Humble or [MCR2 virtual machine](https://manchesterrobotics-my.sharepoint.com/:u:/g/personal/mario_mtz_manchester-robotics_com/EWcRInLzqDZNpxqWlH3X0sQBGXgbTSj9Qp1VX7O_sGy4zQ?e=AMOocL).
* Knowledge of ROS.
* Knowledge of Windows. 
* Basic knowledge of Ubuntu (recommended).
* Basic understanding of robotics (recommended).
* Access to a Puzzlebot Jetson Edition.

## Weekly Sessions
### Week 1: Mobile Robots – Fundamentals
This week the student will learn to basics of mobile robotics.
* Introduction to mobile robotics.
* Puzzlebot
* Robot assembly
* Image installation
* Hackerboard firmware

#### Hackerboard firmware

Update the firmware of the hackerboard inside the [**FirmwareBin**](https://manchesterrobotics-my.sharepoint.com/:u:/g/personal/mario_mtz_manchester-robotics_com/EYJ072eVLwpHhWIp62lGpWcBS3EbZURRDtrQg4JRPyAZrg?e=TcBZDg) zip file.
Follow the instructions for your OS.

#### Balena Etcher and puzzlebot image

Install [Balena Etcher](https://etcher.balena.io/) to format an SD card.

Get the Puzzlebot image and flash it. [Option 1](https://manchesterrobotics-my.sharepoint.com/:u:/g/personal/mario_mtz_manchester-robotics_com/EVMUSVxzaepInxdKvzXnhpQBlhEpad4ZZDCQylmIlI3PlQ?e=5eqEzd) [Option 2](https://www.dropbox.com/scl/fi/2ccqhr9g0u5rj15ysr93r/jetson_2gb_ubuntu20.zip?rlkey=5iq4ebmrf529t5t2jztprsvhp&dl=0)

#### Connect to the Puzzlebot via SSH
* Connect to the puzzlebot-jetson network
* Password: Puzzlebot72  

* Connect via SSH 
        ssh puzzlebot@10.42.0.1
* Password: Puzzlebot72

**Mini challenge:** 
ROS2-Puzzlebot Joystick Activity (Professors in Campus) Drive the Puzzlebot using the joystick package.

### Week 2: Open Loop Control
This week will introduce some basics of open loop control for mobile robotics.
  * Open Loop Robot Control of the Puzzlebot (Theory/Activity)

**Mini challenge:** Multi point navigation with open Loop control. 

### Week 3: Closed Loop Control
This week will be dedicated to the closed loop control in robotics.
 * Localization: odometry
 * Closed Loop Control
 * Point to point navigation.

**Mini challenge:** Multiple point navigation.  

### Week 4: Open CV
This week will be dedicated to the usage of OpenCV for robotics.
* OpenCV introduction and outline
* Interfacing with camera.
* Image filtering and preprocessing 

**Midterm challenge:** Multiple point navigation with image identification.

### Week 5: Midterm Challenge
Midterm challenge

**Midterm challenge:** Multiple point navigation with image identification.

### Week 6: Line Following
This week the algorithms for line following will be teached.
  * Open CV image processing
  * Line Following
    
  **Mini challenge:** Line Following Activity.

### Week 7: Neural Networks
This week is dedicated to the implementation of Neural Networks for robotics.
  * Introduction to neural networks
  * YOLO
  * Remote testing of the NN
 
  **Mini challenge:** Deploy a CNN into a ROS to perform image classification.

### Week 8: Final Challenge
This week MCR2 will introduce the final challenge

### Week 9: Final Challenge
Q&A Week


### Week 10: Final Challenge
Evaluation

## Useful Links: 
  ### Ubuntu
   * [Ubuntu Installation](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
  
  ### ROS
   * [ROS Installation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
   * [ROS book](https://github.com/fmrico/book_ros2)
   * [ROS Packages](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html)
   * [ROS Workspace](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)
   * [ROS Nodes](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)
   * [Topics](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)
   * [Publisher and Subscribers](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)
   * [ROS Launch](https://docs.ros.org/en/humble/How-To-Guides/Launch-file-different-formats.html)
   * [ROS Custom Interfaces](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html)
   * [Parameters](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-Python.html)

  ### Virtual Machine: 
   * [VM Ware](https://customerconnect.vmware.com/en/downloads/details?downloadGroup=WKST-PLAYER-1750&productId=1377&rPId=111473)
   * [ROS Preinstalled VM](https://manchesterrobotics-my.sharepoint.com/:u:/g/personal/mario_mtz_manchester-robotics_com/EWcRInLzqDZNpxqWlH3X0sQBGXgbTSj9Qp1VX7O_sGy4zQ?e=sIq2xd)

  ### Resources
   * [Introduction to Autonomous Mobile Robots](https://ieeexplore.ieee.org/book/6267528)
   * [PID Control](https://ieeexplore.ieee.org/document/1453566)
   * [Closed Loop Control](https://www.electronics-tutorials.ws/systems/closed-loop-system.html)
   * [Nonlineraities and robustness](https://ieeexplore.ieee.org/document/8603065)
   * [Open loop control Tutorial](https://www.electronics-tutorials.ws/systems/open-loop-system.html)
   * [Open Loop Control Tutorial](https://www.electronicshub.org/open-loop-system/)
   * [Open Loop Control Book](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling/Introduction_to_Linear_Time-Invariant_Dynamic_Systems_for_Students_of_Engineering_(Hallauer)/14%3A_Introduction_to_Feedback_Control/14.02%3A_Definitions_and_Examples_of_Open-Loop_Control_Systems)
   * [YOLO](https://docs.google.com/presentation/d/11JtJl12eSv3J0pfxqPnVVl1lCCiL6e6O/edit#slide=id.p1)
   * [YOLO Mendívil](https://drive.google.com/file/d/1ZR5iY6Gcp1_zieyu1k-vYuvBllR8Uk2A/view)
   * [Workshop Deep Learning](https://drive.google.com/drive/folders/1WKCWUSrg49acZxxNBa7DRM3goYYp-JLm)
   * [TinyML](https://www.oreilly.com/library/view/tinyml/9781492052036/ch04.html)
