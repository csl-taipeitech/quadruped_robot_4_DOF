from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    # Define the path to the RViz configuration file
    rviz_config_path = os.path.join(
        '/home/pangolin/pangolin_ws/src/quadruped_robot_4_DOF/pangolin_navigation/pangolin_visual_nav/rviz',
        'apriltag_navigation.rviz'  
    )

    return LaunchDescription([
        # Node for pangolin_visual_nav
        Node(
            package='pangolin_visual_nav',
            executable='pangolin_visual_nav',
            name='pangolin_visual_nav_node',
            output='screen'
        ),
        # Node for goal_pose_visualization
        Node(
            package='pangolin_visual_nav',
            executable='goal_pose_visualization',
            name='goal_pose_visualization_node',
            output='screen'
        ),
        # Node for launching RViz2
        ExecuteProcess(
            cmd=['rviz2', '-d', rviz_config_path],
            output='screen'
        ),
    ])

