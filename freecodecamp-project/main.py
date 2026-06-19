import os
import medical_data_visualizer

# Print current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Generate and save plots
catplot_fig = medical_data_visualizer.draw_cat_plot()
heatmap_fig = medical_data_visualizer.draw_heat_map()

print("Plots generated! Check the folder for catplot.png and heatmap.png")