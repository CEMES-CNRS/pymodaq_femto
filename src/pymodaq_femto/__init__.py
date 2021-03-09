from pathlib import Path
from pyqtgraph.graphicsItems.GradientEditorItem import Gradients
from collections import OrderedDict

# #### including dscan
from pypret.pnps import _PNPS_CLASSES
_PNPS_CLASSES.pop('dscan')
from pymodaq_femto.dscan import DSCAN
# ############

try:
    with open(str(Path(__file__).parent.joinpath('VERSION')), 'r') as fvers:
        __version__ = fvers.read().strip()

    Gradients.update(OrderedDict([
        ('femto', {'ticks': [(0.0, (0, 0, 0, 255)), (0.085, (255, 85, 255, 255)), (0.25, (0, 0, 255, 255))
                             , (0.41, (85, 255, 255, 255)), (0.59, (32, 179, 37, 255)), (0.72, (255, 255, 0, 255))
                             , (0.88, (255, 0, 0, 255)), (1, (255, 255, 255, 255)),], 'mode': 'rgb'}), ]))


except Exception as e:
    print(str(e))
