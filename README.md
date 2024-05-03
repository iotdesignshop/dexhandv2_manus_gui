# dexhand_manus_gui

This repository contains a simple control GUI for managing the dexhand_manus ROS 2 Node.

## Usage

This package is designed to work in conjunction with the following packages:

- **dexhand_ros2_meta** - The metapackage containing the DexHand ROS 2 nodes for description, simulations, etc. 
- **manus_ros2** - ROS 2 package for reading data from the Manus SDK and converting the poses into ROS 2 messages.
- **dexhand_manus** - Adapter for converting manus_ros2 messages into DexHand joint_state messages

To use this GUI, follow these steps:

1. Clone the repository to your dexhand ROS 2 workspace (typically created via the dexhand_ros2_meta package):

    ```bash
    cd <Your dexhand workspace folder>/src
    git clone https://github.com/iotdesignshop/dexhand_manus_gui.git
    ```

2. Build the ROS 2 workspace:

    ```bash
    cd <Your dexhand workspace folder>
    colcon build
    ```

3. Source the ROS 2 environment:

    ```bash
    source install/setup.bash
    ```

4. Launch the Manus/DexHand simulation launch file

    ```bash
    ros2 launch dexhand_manus simulation.launch.py
    ```

    This will start the GUI and you can use it to control the dexhand_manus ROS 2 Node.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.