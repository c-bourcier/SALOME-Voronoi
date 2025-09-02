import sys
import os
import salome_pluginsmanager

def init():
  # Voronization via vorpalite
  try:
    from qtsalome import QIcon
    import Voronoi_converter
    icon_file = os.path.join(os.getenv('GEOGRAMPLUGIN_ROOT_DIR'),'mesh_plugins_geogram.png')
    salome_pluginsmanager.AddFunction('Polyhedralize',
                                      'Generate polyhedral mesh',
                                      Voronoi_converter.convertForCVTCalculation,
                                      icon=QIcon(icon_file))
  except Exception as e:
    salome_pluginsmanager.logger.info('ERROR: Polyhedralize plug-in is unavailable: {}'.format(e))
    print(e)
    pass

