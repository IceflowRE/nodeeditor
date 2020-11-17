"""
Use '-DCMAKE_TOOLCHAIN_FILE=conan_paths.cmake'.
"""

from conans import ConanFile


class NodeeditorConan(ConanFile):
    settings = (
        "os",
        "compiler",
        "build_type",
        "arch"
    )
    requires = (
        "qt/5.15.0@bincrafters/stable",
    )
    generators = "cmake_find_package", "cmake_paths"
    default_options = {
        "qt:shared": True,
        # svg support
        "qt:qtsvg": True,
        # turn off database support
        "qt:with_mysql": False,
        "qt:with_sqlite3": False,
        "qt:with_pq": False,
        "qt:with_odbc": False,
    }

    keep_imports = True

    def imports(self):
        self.copy("*.dll", src="bin", dst="bin")
        self.copy("*.pdb", src="bin", dst="bin")
        self.copy("*.so*", src="lib", dst="bin")
        self.copy("*.dylib*", src="lib", dst="bin")
        self.copy("*", src="plugins", dst="bin")  # get Qt5 platform plugins
