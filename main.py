import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from data_cleaning import clean_data
from data_analysis import perform_analysis
from data_visualization import plot_data, plot_predictions

class DataAnalysisTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Data Analysis Tool")
        
        self.load_button = tk.Button(root, text="Load Data", command=self.load_data)
        self.load_button.pack()
        
        self.clean_button = tk.Button(root, text="Clean Data", command=self.clean_data, state=tk.DISABLED)
        self.clean_button.pack()
        
        self.analyze_button = tk.Button(root, text="Analyze Data", command=self.analyze_data, state=tk.DISABLED)
        self.analyze_button.pack()
        
        self.plot_button = tk.Button(root, text="Plot Data", command=self.plot_data, state=tk.DISABLED)
        self.plot_button.pack()
        
        self.df = None
        self.model = None
        self.X_test = None
        self.y_test = None
    
    def load_data(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.df = pd.read_csv(file_path)
            messagebox.showinfo("Info", "Data Loaded Successfully")
            self.clean_button.config(state=tk.NORMAL)
            self.plot_button.config(state=tk.NORMAL)
    
    def clean_data(self):
        if self.df is not None:
            self.df = clean_data(self.df)
            messagebox.showinfo("Info", "Data Cleaned Successfully")
            self.analyze_button.config(state=tk.NORMAL)
    
    def analyze_data(self):
        if self.df is not None:
            target_column = 'target'  # Replace with your target column
            self.model, self.X_test, self.y_test = perform_analysis(self.df, target_column)
            messagebox.showinfo("Info", "Data Analysis Completed")
    
    def plot_data(self):
        if self.df is not None:
            plot_data(self.df)
        if self.model is not None:
            plot_predictions(self.model, self.X_test, self.y_test)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisTool(root)
    root.mainloop()
