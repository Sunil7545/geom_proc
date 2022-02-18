import pyvista as pv


def read_visualize_point_set():
    """
    This method reads the points set and renders them.
    :return: None
    """
    # viewer window
    plotter = pv.Plotter(off_screen=False, window_size=[700, 700])
    file_name = r"point_set.obj"
    data_reader = pv.get_reader(file_name)
    pv_data = data_reader.read()
    plotter.add_mesh(pv_data, smooth_shading=False, color='orange', render_points_as_spheres=True)
    plotter.set_background([1, 1, 1])
    plotter.show()


def surface_reconstruction():
    """
    This method reads points set, reconstructs the corresponding triangular mesh and then renders it.
    :return: None
    """
    plotter = pv.Plotter(off_screen=False, window_size=[700, 700])
    file_name = r"point_set.obj"
    data_reader = pv.get_reader(file_name)
    pv_data = data_reader.read()
    points = pv.wrap(pv_data.points)
    surf = points.reconstruct_surface()
    plotter.add_mesh(surf, show_edges=True, smooth_shading=False, color='orange', render_points_as_spheres=True)
    plotter.set_background([1, 1, 1])
    plotter.show()


def surface_smoothing():
    """
     This method reads points set, reconstructs the corresponding triangular mesh, removes noise components,
      and then renders it.
    :return:
    """
    plotter = pv.Plotter(off_screen=False, window_size=[700, 700])
    file_name = r"point_set.obj"
    data_reader = pv.get_reader(file_name)
    pv_data = data_reader.read()
    points = pv.wrap(pv_data.points)
    surf = points.reconstruct_surface()
    surf = surf.smooth(n_iter=100)
    plotter.add_mesh(surf, show_edges=False, smooth_shading=False, color='orange', render_points_as_spheres=False)
    plotter.set_background([1, 1, 1])
    plotter.show()


def feature_extraction():
    """
    This method reads a mesh, extracts features and then render features along with the mesh
    :return:
    """
    plotter = pv.Plotter(off_screen=False, window_size=[700, 700])
    file_name = r"block.obj"
    data_reader = pv.get_reader(file_name)
    pv_data = data_reader.read()
    edges = pv_data.extract_feature_edges(40)
    plotter.add_mesh(pv_data, show_edges=False, smooth_shading=False, color='orange', render_points_as_spheres=False)
    plotter.add_mesh(edges, color=[0, 0.3, 1], line_width=5)
    plotter.set_background([1, 1, 1])
    plotter.enable_anti_aliasing()
    plotter.show()


if __name__ == "__main__":
    read_visualize_point_set()
    surface_reconstruction()
    surface_smoothing()
    feature_extraction()



