# Build-in libraries.
import time

# Third-party libraries.
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd


def graph(inverter, param_array, graph_time=10000.0,
          labels=None, colors=None,
          grid=True, grid_args=[],
          save=False, filepath=None):
    """ This function can be used to generate a
    graphical view of inverter variables using matplotlib.

    ARGUMENTS
    -----------
    - inverter is a Sinamics object defined via sinamics.py.
    - param_array is a list of lists. Each list has the
      same format as the arguments of method read_parameter
      in sinamics.py main code.
    - graph_time is the time that the trace will last in ms.
    - labels can be defined as a list with same len as param_array
      containing the label strings for each parameter
      to be traced. If equal None them the parameter number is selected.
    - colors can define the color for each parameter to be traced.
      More info on how you can customize this parameter, see:
      https://matplotlib.org/3.1.0/tutorials/colors/colors.html
      If equal None :
          xkcd colors are used
    - grid equal True means a grid will be displayed in the graph.
    - grid_args can be a list containing the
      arguments to be passed to grid pyplot method
      with exception of the main grid=True.
      More info on these arguments can be seen in:
      https://matplotlib.org/3.1.1/api/as_gen/matplotlib.pyplot.grid.html
    - using save=true, you can save the graph as a file
      with a path and name specified in 'filepath' argument, e.g.:
      filepath='<Directory>/graph1.png'. Not all file types are accepted.
      For complete details on accepted types, see:
      https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.savefig.html

    RETURNS
    -----------
    - A tuple containing the collect array data [0] and time axis [1].

    EXAMPLE
    -----------
    Generating a graph of unfiltered variables, speed (r0021),
    current (r0027) and DC link (r0026) for 10 seconds.

    import sinamics

    g120 = sinamics.Sinamics()
    g120.connect('192.168.0.20')
    param_array = [[21, 'f'], [27, 'f'], [26, 'f']]
    g120.graph(param_array, graph_time=10000.0)

    """

    # Initial values.
    read_data_array = [[] for i in range(0, len(param_array))]
    time_axis = []
    start_time = time.time() * 1000.0  # Converting to miliseconds.
    run_time = start_time

    # Gathering data
    while (run_time-start_time < graph_time):
        i = 0
        for item in param_array:
            read_data_array[i].append(inverter.read_parameter(*item))
            i += 1
        run_time = time.time() * 1000.  # Converting to miliseconds.
        time_axis.append(run_time-start_time)

    # Defining labels.
    if type(labels) is list and len(labels) == len(param_array):
        labels = labels
    else:
        # The label will be 'r' + parameter number.
        labels = ['r'+str(param_array[i][0])
                  for i in range(0, len(param_array))]

    # Defining colors.
    if type(colors) is list and len(colors) == len(param_array):
        colors = colors
    else:
        colors = [color for color in mcd.XKCD_COLORS][0:len(param_array)]

    # Plotting.
    # More info on the plotting of multiple axes in same figure, see:
    # https://matplotlib.org/gallery/api/two_scales.html
    fig, host = plt.subplots(figsize=(10, 10))
    # Each index of 'plots' may be a graph of a variable.
    plots = [0 for i in range(0, len(param_arary))]
    i = 0  # counter for loop

    for data in read_data_array:
        if i == 0:
            # First plot and host for next plots.
            host.set_xlabel('Time (ms)')
            host.set_ylabel(labels[i], color=colors[i])
            host.plot(time_axis, data, color=colors[i])
            host.tick_params(axis='y', labelcolor=colors[i])
        else:
            # Plots sharing the same X axis with the host (twins).
            plots[i-1] = host.twinx()
            plots[i-1].set_ylabel(labels[i], color=colors[i])
            plots[i-1].plot(time_axis, data, color=colors[i])
            plots[i-1].tick_params(axis='y', labelcolor=colors[i])
        if i > 1:
            # Horizontal offset in Y scale of twin plots.
            plots[i-1].spines['right'].set_position(('outward',
                                                     (i-1)*70))
        i += 1
    fig.tight_layout()  # For better appereance of Y scales.

    # Setting grid.
    plt.grid(grid, *grid_args)

    # Saving or showing.
    if save and filepath is not None:
        plt.savefig(filepath)
    else:
        plt.show()

    return (read_data_array, time_axis)
