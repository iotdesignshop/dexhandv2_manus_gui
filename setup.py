from setuptools import find_packages, setup

package_name = 'dexhand_manus_gui'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dexhand',
    maintainer_email='trent@iotdesignshop.com',
    description='Simple GUI for Controlling dexhand_manus node features',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gui_node = dexhand_manus_gui.gui_node:main'
        ],
    },
)
