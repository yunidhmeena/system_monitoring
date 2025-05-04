import psutil
import matplotlib.pyplot as plt

try:
    cpu_usage = psutil.cpu_percent(interval=5)
    
    memory = psutil.virtual_memory()
    memory_usage=memory.percent
    
    disk=psutil.disk_usage('/')
    disk_usage=disk.percent
    
    print (f'CPU USAGE: {cpu_usage}%')
    print (f'MEMORY USAGE: {memory_usage}%')
    print (f'DISK USAGE:{disk_usage}%')
    
    # Create a bar chart to visualize CPU, memory, and disk usage
    categories = ['CPU', 'Memory', 'Disk']
    values = [cpu_usage, memory_usage, disk_usage]
    
    plt.bar(categories, values)
    bar_color = {'red'}
    plt.bar(categories, values, color=bar_color)
    background_color = 'black'
    plt.gca().set_facecolor(background_color)

    plt.bar(categories, values)
    plt.xlabel('Resource')
    plt.ylabel('Usage (%)')
    plt.title('System Resource Usage')
    plt.show()

except Exception as e:
    print(f"An error occurred: {str(e)}")