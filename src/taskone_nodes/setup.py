from setuptools import find_packages, setup

package_name = 'taskone_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aadya_prasad',
    maintainer_email='aadya_prasad@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'taskone_publisher = taskone_nodes.taskone_publisher:main',
            'taskone_subscriber = taskone_nodes.taskone_subscriber:main',
        ],
    },
)
