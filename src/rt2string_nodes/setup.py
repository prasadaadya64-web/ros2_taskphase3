from setuptools import find_packages, setup

package_name = 'rt2string_nodes'

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
            'string_publisher = rt2string_nodes.string_publisher:main',
            'palindrome_checker = rt2string_nodes.palindrome_checker:main',
            'result_converter = rt2string_nodes.result_converter:main',
        ],
    },
)
