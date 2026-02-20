# Sorting Visualizer

This project visualizes various sorting algorithms, allowing users to see the steps involved in sorting elements in an array. The visualization uses different sorting algorithms, and each step is shown with animated transitions.

## Features

- **Sorting Algorithms Visualization**: Supports visualizing various sorting algorithms, including Bubble Sort, Quick Sort, Merge Sort, etc.
- **Interactive UI**: The user can select sorting algorithms, configure settings, and view animations of the sorting process.
- **Animation**: Each sorting step is animated for clarity, with smooth transitions between steps.
- **Customizable**: Users can configure the sorting speed, array size, and other settings.

## Project Structure

### **animation/**
Contains the core animation logic for visualizing the sorting process.

- **Animation.py**: Manages animation of the sorting process.

### **block/**
Handles the visual representation of the array elements as blocks.

- **Block.py**: Defines how the blocks are drawn and updated during the sorting.

### **datastructure/**
Handles data structures related to the sorting process.

- **Arrayblock.py**: Deals with the representation of arrays and blocks during sorting.

### **uicomponents/**
UI components and tools for user interaction.

- **AnalysisSpace.py**: UI component for the sorting analysis space.
- **Board.py**: Represents the sorting board or canvas.
- **DrawingCanvas.py**: Handles the drawing of the blocks on the canvas.
- **Menubar.py**: Contains the menu bar logic for user settings.
- **ToolTip.py**: Provides tooltips for information and interaction.

### **window/**
Handles the configuration window and related settings.

- **ConfigWindow.py**: Manages the configuration window where users can set the sorting parameters.

## Requirements

- Python 3.x
- Required libraries (e.g., `tkinter`, `numpy`)
