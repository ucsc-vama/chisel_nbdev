from distutils.core import setup
setup(
    entry_points = {
        'nbconvert.exporters': [
            'scala = scala_conv:ScalaExporter',
        ],
    }
)