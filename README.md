#Task Scheduling App - DSA Mini Project

Team Members:

Harsh Bhardwaj (Team Lead)

Harsh Chand Srivastava

Harshita Gupta

Krishna Tiwari

Project Overview:

This Task Scheduling App is a simple yet effective tool designed to help users manage tasks based on their priority. The application allows users to:


Add tasks with a priority.

Retrieve the highest priority task.

Delete all tasks from the list.

The app uses a Priority Queue to store and manage tasks efficiently, ensuring that tasks with the highest priority are processed first.

Technologies Used:

Python

Tkinter (for GUI development)

Data Structures: Priority Queue

Key Features:

Add Task: Users can add a task with a name and a priority. Tasks are inserted in sorted order based on their priority (higher priority first).

Get Next Task: Users can view and retrieve the task with the highest priority.

Delete All Tasks: Users can clear all tasks from the queue.

Main Functionalities:


Add tasks.

View tasks sorted by priority.

Execute tasks in the correct order.


Graphical User Interface: A simple and intuitive interface built with Tkinter, providing an easy-to-use experience.

Code Structure:

PriorityQueue Class:


Implemented by: Harshita Gupta and Krishna Tiwari

This class handles the core functionality of the priority queue, including adding tasks, retrieving the highest priority task, and clearing all tasks.

Tkinter Interface:

Developed by: Harsh Bhardwaj and Harsh Chand Srivastava

This part of the project creates the user interface for the app, including input fields for tasks and priorities, buttons for operations, and a list box to display the tasks.

How to Run the Application:

Ensure you have Python 3.x installed on your machine.

Download or clone the project repository.

Install Tkinter if not already installed (Tkinter is usually bundled with Python).

Run the Python script to launch the Task Scheduling App.

bash:Copy code

$python task_scheduler.py
