import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time
from window.ConfigWindow import ConfigWindow


class AnalysisSpace(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(bg="#000000")
        # Add your analysis space widgets and layout here
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        lesser = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return self.quicksort(lesser) + equal + self.quicksort(greater)

    def timsort(self, arr):
        arr.sort()

    def plot_scatter_graph(self):
        # Initialize lists to store values
        n_values = []
        time_taken = []

        # Perform sorting algorithm for different n values
        for n in range(0, 1001):
            # Generate a random list of n elements
            arr = [random.randint(1, 1000) for _ in range(n)]

            # Measure the time taken for sorting
            start_time = time.time()
            self.merge_sort(arr)
            # Perform your sorting algorithm here
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Append n and time taken to the lists
            n_values.append(n)
            time_taken.append(elapsed_time)

        # Create scatter plot
        fig, ax = plt.subplots()
        ax.scatter(n_values, time_taken, alpha=0.5)
        ax.set_title("Sorting Algorithm Analysis")
        ax.set_xlabel("n")
        ax.set_ylabel("Time Taken (seconds)")

        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=0)
