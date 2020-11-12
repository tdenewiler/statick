"""Discovery plugin to find ROS packages."""
import os
from typing import Optional

from statick_tool.discovery_plugin import DiscoveryPlugin
from statick_tool.exceptions import Exceptions
from statick_tool.package import Package


class RosDiscoveryPlugin(DiscoveryPlugin):
    """Discovery plugin to find ROS packages."""

    def get_name(self) -> str:
        """Get name of discovery type."""
        return "ros"

    def scan(
        self, package: Package, level: str, exceptions: Optional[Exceptions] = None
    ) -> None:
        """Scan package looking for ROS package files."""
        cmake_file = os.path.join(package.path, "CMakeLists.txt")
        package_file = os.path.join(package.path, "package.xml")

        if os.path.isfile(cmake_file) and os.path.isfile(package_file):
            print("  Package is ROS.")
            package["ros"] = True
            if os.getenv("ROS_VERSION") == "2":
                distro = os.getenv("ROS_DISTRO")
                for path in os.getenv("PATH").split(":"):
                    if distro is not None and distro in path:
                        package["cmake_flags"] = "-DCMAKE_PREFIX_PATH=" + path.rstrip(
                            "/bin"
                        )
                        print("  Adding CMake flags: {}".format(package["cmake_flags"]))
        else:
            print("  Package is not ROS.")
            package["ros"] = False
